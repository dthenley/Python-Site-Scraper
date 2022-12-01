from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://www.dahlkefinancialks.com/learning_center/research/"
page = requests.get(url)
page = page.content

soup = BeautifulSoup(page, 'html.parser')

ul = soup.find('div', class_='custom eme_block')

articles = ul.find_all( 'li', class_='content_item' )
blogs = []
for article in articles:
    title = article.find('a').text
    excerpt = article.find('p').text
    link = article.find('a').attrs['href']
    newurl = f"https://www.dahlkefinancialks.com{link}"
    newpage = requests.get(newurl)
    newsoup = BeautifulSoup(newpage.content, 'html.parser')
    articleContent = newsoup.find('div', {'id': 'Content_container'})
    image = articleContent.find('img').attrs['src']
    articleContent = str(articleContent)
    blogs.append([title,excerpt, image, articleContent])
    
df = pd.DataFrame(blogs, columns=['Title', 'Excerpt', 'Image', 'Article'])

df.to_csv('articles.csv')