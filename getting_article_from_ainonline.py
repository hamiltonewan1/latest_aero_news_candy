import requests
from bs4 import BeautifulSoup

url = 'https://www.ainonline.com/'

page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

titles_html_aironline = soup.find_all(class_='field-content title')
texts_html_aironline = soup.find_all(class_='tile-description', itemprop='description')
urls_html_aironline = soup.find_all(class_='field-content title')
pics_html_aironline = soup.find_all(class_='field-content ain30-thumbnail')
dates_html_aironline = soup.find_all(class_='date-display-single')


articles_aironline = [
	['title', 'text', 'url', 'picture', 'date', 'www.ainonline.com'],
	['title', 'text', 'url', 'picture', 'date', 'www.ainonline.com'],
	['title', 'text', 'url', 'picture', 'date', 'www.ainonline.com'],
	['title', 'text', 'url', 'picture', 'date', 'www.ainonline.com'],
	['title', 'text', 'url', 'picture', 'date', 'www.ainonline.com'],#5
	['title', 'text', 'url', 'picture', 'date', 'www.ainonline.com'],
	['title', 'text', 'url', 'picture', 'date', 'www.ainonline.com'],
	['title', 'text', 'url', 'picture', 'date', 'www.ainonline.com'],
	['title', 'text', 'url', 'picture', 'date', 'www.ainonline.com'],
	['title', 'text', 'url', 'picture', 'date', 'www.ainonline.com']]#10
	

for i in range(0,10):
	articles_aironline[i][0] = str(titles_html_aironline[i]).split('>')[2].split('<')[0]
	articles_aironline[i][1] = ''
	articles_aironline[i][2] = 'https://www.ainonline.com' + str(urls_html_aironline[i]).split('">')[1].split('="')[1]
	try:
		articles_aironline[i][3] = str(pics_html_aironline[i]).split('src="')[1].split('?itok')[0]
	except:
		articles_aironline[i][3] = 'https://i.ibb.co/n3fSDq7/placeholder.png'
	articles_aironline[i][4] = str(dates_html_aironline[i]).split('content="')[1].split('T')[0]
 