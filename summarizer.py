import pandas as pd
from transformers import pipeline
import os

cwd = os.getcwd()
os.environ['TRANSFORMERS_CACHE'] = os.path.join(cwd, 'transformers_cache')
summarizer = pipeline("summarization")

df = pd.read_csv("my_scraped_articles.csv")
num_rows = len(df)
summarizer = pipeline("summarization", model="facebook/bart-large-cnn", tokenizer="facebook/bart-large-cnn")


for i in range(3, len(df)):
    article = df.loc[i,'Text']

    try:
        summary = summarizer(article, max_length=100, min_length=10, do_sample=False)
    except IndexError:
        print("bro I don't know why this is happening but needs to be debugged\n\n\n\n")

    print("- " + summary[0]['summary_text'].replace('. ', '.\n- '))
    print()
    print()