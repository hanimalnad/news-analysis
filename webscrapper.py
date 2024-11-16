import newspaper
from newspaper import Article
from newspaper import Source
from newspaper import news_pool
import pandas as pd

ndtv = newspaper.build('https://www.ndtv.com/news', memoize_articles=False)
tv9 = newspaper.build("https://www.news9live.com/", memoize_articles=False)

papers = [ndtv, tv9]

news_pool.set(papers, threads_per_source=4)

news_pool.join()

final_df = pd.DataFrame()

limit = 100

for source in papers:
    list_title = []
    list_text = []
    list_source =[]

    count = 0

    for article_extract in source.articles:
        article_extract.parse()

        if count > limit:
            break         

        list_title.append(article_extract.title)
        list_text.append(article_extract.text)
        list_source.append(article_extract.source_url)

        count +=1


    temp_df = pd.DataFrame({'Title': list_title, 'Text': list_text, 'Source': list_source})
    final_df = pd.concat([final_df, temp_df], ignore_index=True)
    
final_df.to_csv('my_scraped_articles.csv')