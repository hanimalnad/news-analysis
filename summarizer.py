import pandas as pd
from transformers import pipeline

summarizer = pipeline("summarization")

df = pd.read_csv("my_scraped_articles.csv")

article = (df.loc[3,'Text'])

summary = summarizer(article, max_length=50, min_length=10, do_sample=False)

print("- " + summary[0]['summary_text'].replace('. ', '.\n- '))


