import nltk
from newspaper import Article
import requests

def summary(url):
    article = Article(url)
    article.download()
    article.parse()
    nltk.download('punkt')
    article.nlp()
    # print(article.authors)
    # print(article.publish_date)
    # print(article.text)
    print(article.publish_date)
    print(article.top_image)
    return article.summary,article.top_image
#
# url = input()
# article = Article(url)
#
# article.download()
# article.parse()
# nltk.download('punkt')
# article.nlp()
#
# print(article.authors)
# print(article.publish_date)
# # print(article.text)
# print(article.summary)