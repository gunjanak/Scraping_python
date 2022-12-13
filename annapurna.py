from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests


#opening the annapurna express
path = 'https://theannapurnaexpress.com'
r = requests.get(path)
print(r.status_code)


#creating a beautiful soup object
bs = BeautifulSoup(r.content,'html.parser')



#Reading the headline
output = bs.find(class_="news-body")
print('Headline')
print(output.a.text)

#Finding the link of page containg headline news in detail
print('\n................\n')
print('Link for the headline')
link_for_full_article = output.a.get('href')
link_for_full_article = path + link_for_full_article
print(link_for_full_article)


#Visiting this new link
print('\n................\n')
print('Visiting full article page')
full_article_html = requests.get(link_for_full_article)
bs_full_article = BeautifulSoup(full_article_html.content,'html.parser')

#Reading its detalis
output_full_article = bs_full_article.find(class_="article-content-wrapper")

#output_full_article = output_full_article[3]


paragraphs = output_full_article.find_all("p")
print(len(paragraphs))
for paragraph in paragraphs:
    print(paragraph.text)
    print('\n...............\n')




