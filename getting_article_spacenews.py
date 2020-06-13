import requests
from bs4 import BeautifulSoup

url = 'https://spacenews.com/segment/news/'

page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

title_html_spacenews = soup.find_all(class_='launch-title')
text_html_spacenews = soup.find_all(class_='post-excerpt')
url_html_spacenews = soup.find_all(class_='launch-title')
pics_html_spacenews = soup.find_all(class_='launch-image')
date_html_spacenews = soup.find_all(class_='launch-author')

articles_spacenews = [
	['title', 'text', 'url', 'picture', 'date', 'www.spacenews.com'],
	['title', 'text', 'url', 'picture', 'date', 'www.spacenews.com'],
	['title', 'text', 'url', 'picture', 'date', 'www.spacenews.com'],
	['title', 'text', 'url', 'picture', 'date', 'www.spacenews.com'],
	['title', 'text', 'url', 'picture', 'date', 'www.spacenews.com'],#5
	['title', 'text', 'url', 'picture', 'date', 'www.spacenews.com'],
	['title', 'text', 'url', 'picture', 'date', 'www.spacenews.com'],
	['title', 'text', 'url', 'picture', 'date', 'www.spacenews.com'],
	['title', 'text', 'url', 'picture', 'date', 'www.spacenews.com'],
	['title', 'text', 'url', 'picture', 'date', 'www.spacenews.com']]#10

for i in range(0,10):
	articles_spacenews[i][0] = str(title_html_spacenews[i]).split('>')[2].split('<')[0]
	articles_spacenews[i][1] = str(text_html_spacenews[i]).split('>')[1].split('<')[0]
	articles_spacenews[i][2] = str(url_html_spacenews[i]).split('>')[1].split('"')[1]
	articles_spacenews[i][3] = str(pics_html_spacenews[i]).split('"')[11]
	articles_spacenews[i][4] = str(date_html_spacenews[i]).split('"')[13]



