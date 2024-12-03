from flask import Flask, jsonify
import newspaper
from newspaper import Article
from newspaper import Source
from newspaper import news_pool
import pandas as pd
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification
import os
from flask_cors import CORS
from textblob import TextBlob

app = Flask(__name__)
CORS(app)

@app.route('/scrape', methods=['GET'])
def scraper():
    if os.path.isfile("/app/my_scraped_articles.csv"):
        os.remove("/app/my_scraped_articles.csv")
    
    ndtv = newspaper.build('https://www.ndtv.com/news', memoize_articles=False)
    tv9 = newspaper.build("https://www.news9live.com/", memoize_articles=False)

    papers = [ndtv, tv9]
    news_pool.set(papers, threads_per_source=4)
    news_pool.join()

    final_df = pd.DataFrame()
    limit = 50

    for source in papers:
        list_title = []
        list_text = []
        list_source = []
        list_images = []
        count = 0

        for article_extract in source.articles:
            try:
                article_extract.download()
                article_extract.parse()

                if count >= limit:
                    break
                
                list_title.append(article_extract.title)
                list_text.append(article_extract.text)
                list_source.append(article_extract.url)
                list_images.append(article_extract.top_image)
                count += 1
            except Exception as e:
                print(f"Error processing article: {e}")
                list_images.append(None) 

        temp_df = pd.DataFrame({'Title': list_title, 'Text': list_text, 'Source': list_source, 'Image': list_images})
        final_df = pd.concat([final_df, temp_df], ignore_index=True)

    final_df.to_csv('/app/my_scraped_articles.csv', index=False)

    return jsonify({"message": "Scraping completed successfully", "articles_scraped": len(final_df)}), 200


@app.route('/summarize', methods=['GET'])
def summarize():
    cwd = os.getcwd()
    os.environ['TRANSFORMERS_CACHE'] = os.path.join(cwd, 'transformers_cache')
    summarizer = pipeline("summarization")

    df = pd.read_csv("/app/my_scraped_articles.csv")
    num_rows = len(df)
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn", tokenizer="facebook/bart-large-cnn")


    for i in range(3, num_rows):
        article = df.loc[i,'Text']

        try:
            summary = summarizer(article, max_length=100, min_length=10, do_sample=False)
        except IndexError:
            print("bro I don't know why this is happening but needs to be debugged\n\n\n\n")

        print("- " + summary[0]['summary_text'].replace('. ', '.\n- '))
        print()
        print()

pipe = pipeline("text-classification", model="cardiffnlp/twitter-roberta-base-topic-latest")

tokenizer = AutoTokenizer.from_pretrained("cardiffnlp/twitter-roberta-base-topic-latest")
model = AutoModelForSequenceClassification.from_pretrained("cardiffnlp/twitter-roberta-base-topic-latest")

@app.route('/categorize', methods=['GET'])
def categorize():
    df = pd.read_csv("my_scraped_articles.csv")

    categories = []

    for i in range(len(df)):
        article = df.loc[i, 'Text']

        if not isinstance(article, str) or pd.isna(article):
            article = ""

        if article.strip():
            result = pipe(article[:512])  
            category = result[0]['label']
        else:
            category = "Uncategorized"
        categories.append(category)

    df['Category'] = categories
    unique_categories = list(set(categories))

    df.to_csv('my_scraped_articles.csv', index=False)

    return jsonify({
        "message": "Categorization completed and saved to CSV.",
        "unique_categories": unique_categories
    }), 200 
        
@app.route('/senti', methods=['GET'])
def senti():
    
    df = pd.read_csv("my_scraped_articles.csv")

    sentiments = []

    for i in range(len(df)):
        article = df.loc[i, 'Text']

        if not isinstance(article, str) or pd.isna(article):
            article = ""  
            
        blob = TextBlob(article)
        polarity = blob.sentiment.polarity

        if polarity > 0:
            sentiment = 'Positive'
        elif polarity < 0:
            sentiment = 'Negative'
        else:
            sentiment = 'Neutral'
            
        sentiments.append(sentiment)

   
    df['Sentiment'] = sentiments
    df.to_csv('my_scraped_articles.csv', index=False)

    return "Sentiment analysis completed and saved to CSV."

    
@app.route('/get_data', methods=['GET'])
def get_data():
    try:
        df = pd.read_csv("my_scraped_articles.csv")
        return df.to_json(orient='records'), 200  
    except FileNotFoundError:
        return jsonify({"error": "CSV file not found. Run the scrape endpoint first."}), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)