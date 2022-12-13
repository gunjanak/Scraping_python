from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests


#opening the annapurna express
path = 'https://kathmandupost.com'
r = requests.get(path,headers={'User-Agent': 'Chrome/108.0.0.0'})
print(r.status_code)
#Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36

#creating a beautiful soup object
bs = BeautifulSoup(r.content,'html.parser')
#print(bs)


#Reading the headline
output = bs.find(class_="1")
output = output.find('h2')
print('Headline')
print(output.text)

#Finding the link of page containg headline news in detail
print('\n................\n')
print('Link for the headline')
link_for_full_article = output.a.get('href')
link_for_full_article = path+link_for_full_article
print(link_for_full_article)

#Visiting this new link
print('\n................\n')
print('Visiting full article page')
full_article_html = requests.get(link_for_full_article,headers={'User-Agent': 'Chrome/108.0.0.0'})
print(full_article_html.status_code)
bs_full_article = BeautifulSoup(full_article_html.content,'html.parser')


output = bs_full_article.find(class_='story-section')
paragraphs = output.find_all("p")
print(len(paragraphs))
for paragraph in paragraphs:
    print(paragraph.text)
    print('\n...............\n')
