from flask import Flask, jsonify
import newspaper
from newspaper import Article
from newspaper import Source
from newspaper import news_pool
import pandas as pd
from transformers import pipeline,  AutoTokenizer, AutoModelForSequenceClassification
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/scrape_and_categorize', methods=['GET'])
def scrape_and_categorize():
    # Remove existing CSV file if it exists
    if os.path.isfile("/app/my_scraped_articles.csv"):
        os.remove("/app/my_scraped_articles.csv")

    # Load previously processed URLs
    processed_urls = set()
    processed_file = "/app/processed_urls.txt"
    if os.path.isfile(processed_file):
        with open(processed_file, 'r') as file:
            processed_urls.update(line.strip() for line in file)

    # Build news sources
    ndtv = newspaper.build('https://www.ndtv.com/news', memoize_articles=False)
    tv9 = newspaper.build("https://www.news9live.com/", memoize_articles=False)
    papers = [ndtv, tv9]

    # Use the newspaper library's thread pool for faster scraping
    news_pool.set(papers, threads_per_source=4)
    news_pool.join()

    # Initialize final DataFrame and limit
    final_df = pd.DataFrame()
    limit = 50

    # Load pre-trained categorization pipeline
    categorizer = pipeline("text-classification", model="cardiffnlp/twitter-roberta-base-topic-latest")

    for source in papers:
        list_title = []
        list_text = []
        list_source = []
        list_images = []
        list_categories = []
        count = 0

        for article_extract in source.articles:
            try:
                # Skip URLs already processed
                if article_extract.url in processed_urls:
                    continue

                # Download and parse the article
                article_extract.download()
                article_extract.parse()

                # Stop scraping from this source after reaching the limit
                if count >= limit:
                    break

                # Extract article details
                title = article_extract.title
                text = article_extract.text
                source_url = article_extract.url
                top_image = article_extract.top_image

                # Categorize the article
                if text.strip():  # Ensure text is non-empty
                    category_result = categorizer(text[:512])  # Truncate to 512 characters for the model
                    category = category_result[0]['label']
                else:
                    category = "Uncategorized"

                # Append details to lists
                list_title.append(title)
                list_text.append(text)
                list_source.append(source_url)
                list_images.append(top_image)
                list_categories.append(category)

                # Add the URL to the processed set
                processed_urls.add(article_extract.url)
                count += 1
            except Exception as e:
                print(f"Error processing article: {e}")
                list_images.append(None)
                list_categories.append("Uncategorized")

        # Create a temporary DataFrame for the current source
        temp_df = pd.DataFrame({
            'Title': list_title,
            'Text': list_text,
            'Source': list_source,
            'Image': list_images,
            'Category': list_categories
        })

        # Append to the final DataFrame
        final_df = pd.concat([final_df, temp_df], ignore_index=True)

    # Save the processed URLs back to the file
    with open(processed_file, 'w') as file:
        for url in processed_urls:
            file.write(url + '\n')

    # Save the scraped articles with categories to a CSV file
    final_df.to_csv('/app/my_scraped_articles.csv', index=False)

    # Return success response
    unique_categories = final_df['Category'].unique().tolist()
    return jsonify({
        "message": "Scraping and categorization completed successfully",
        "articles_scraped": len(final_df),
        "unique_categories": unique_categories
    }), 200


sentiment_analyzer = pipeline("sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment")

@app.route('/senti', methods=['GET'])
def senti():
    try:
        df = pd.read_csv("/app/my_scraped_articles.csv")

        sentiments = []

        for i in range(len(df)):
            article = df.loc[i, 'Text']

            if not isinstance(article, str) or pd.isna(article):
                article = ""  
            
            if article.strip():
                result = sentiment_analyzer(article[:512])  # Limit input length
                sentiment_label = result[0]['label']

                if sentiment_label == 'LABEL_0':
                    sentiment = 'Negative'
                elif sentiment_label == 'LABEL_1':
                    sentiment = 'Neutral'
                elif sentiment_label == 'LABEL_2':
                    sentiment = 'Positive'
                else:
                    sentiment = 'Unknown'
            else:
                sentiment = "Neutral"  # Default for empty articles
            
            sentiments.append(sentiment)

        df['Sentiment'] = sentiments
        df.to_csv('/app/my_scraped_articles.csv', index=False)

        return jsonify({"message": "Sentiment analysis completed and saved to CSV."}), 200
    except FileNotFoundError:
        return jsonify({"error": "CSV file not found. Run the scrape endpoint first."}), 404


@app.route('/get_data', methods=['GET'])
def get_data():
    try:
        df = pd.read_csv("/app/my_scraped_articles.csv")
        return df.to_json(orient='records'), 200
    except FileNotFoundError:
        return jsonify({"error": "CSV file not found. Run the scrape endpoint first."}), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
