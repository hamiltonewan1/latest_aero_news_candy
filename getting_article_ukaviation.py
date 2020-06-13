import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = 'https://ukaviation.news/category/news/'

page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

titles = soup.find_all(class_="entry-title mh-posts-grid-title")
urls = soup.find_all(class_="entry-title mh-posts-grid-title")
pics = soup.find_all(class_="mh-thumb-icon mh-thumb-icon-small-mobile")
dates =soup.find_all(class_="entry-meta-date updated")

articles_ukaviation = [
	['title', 'text', 'url', 'picture', 'date', 'www.ukaviation.news'],
	['title', 'text', 'url', 'picture', 'date', 'www.ukaviation.news'],
	['title', 'text', 'url', 'picture', 'date', 'www.ukaviation.news'],
	['title', 'text', 'url', 'picture', 'date', 'www.ukaviation.news'],
	['title', 'text', 'url', 'picture', 'date', 'www.ukaviation.news'],#5
	['title', 'text', 'url', 'picture', 'date', 'www.ukaviation.news'],
	['title', 'text', 'url', 'picture', 'date', 'www.ukaviation.news'],
	['title', 'text', 'url', 'picture', 'date', 'www.ukaviation.news'],
	['title', 'text', 'url', 'picture', 'date', 'www.ukaviation.news'],
	['title', 'text', 'url', 'picture', 'date', 'www.ukaviation.news']]#10
	
for i in range(0, 10):
	articles_ukaviation[i][0] = str(titles[i]).split('title="')[1].split('">')[0]
	articles_ukaviation[i][2] = str(urls[i]).split('href="')[1].split('"')[0]
	articles_ukaviation[i][3] = str(pics[i]).split('src="')[1].split('?resize')[0]
	dte = str(dates[i]).split('>')[4].split('<')[0]
	articles_ukaviation[i][4] = datetime.strptime(dte, '%d/%m/%Y').strftime('%Y-%m-%d')


