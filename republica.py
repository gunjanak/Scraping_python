from urllib.request import urlopen
from bs4 import BeautifulSoup


#opening the rising nepal url
path = 'https://myrepublica.nagariknetwork.com'
html = urlopen(path)

#creating a beautiful soup object
bs = BeautifulSoup(html.read(),'html.parser')


#Reading the headline
output = bs.find(class_="banner top-breaking")
print('Headline')
headline = output.h2
print(headline.text)
print("\n\n.................\n\n")

#Finding the link of page containg headline news in detail
print('\n................\n')
print('Link for the headline')
link_for_full_article = output.a.get('href')
link_for_full_article = path+link_for_full_article
print(link_for_full_article)

#Visiting this new link
print('\n................\n')
print('Visiting full article page')
full_article_html = urlopen(link_for_full_article)
bs_full_article = BeautifulSoup(full_article_html.read(),'html.parser')

#Reading its detalis
output_full_article = bs_full_article.find(id="newsContent")

#output_full_article = output_full_article[3]


paragraphs = output_full_article.find_all("p")

print(len(paragraphs))

for paragraph in paragraphs:
    print(paragraph.text)
    print('\n...............\n')

