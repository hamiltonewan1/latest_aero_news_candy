import requests
from bs4 import BeautifulSoup
from datetime import datetime

#url = 'https://www.reuters.com/subjects/aerospace-and-defense'

url = 'https://uk.reuters.com/subjects/aerospace-and-defence'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

title_html_reuters = soup.find_all(class_='story-title')
text_html_reuters = soup.find_all(class_='story-content')
url_html_reuters= soup.find_all(class_='story-content')
date_html_reuters = soup.find_all(class_='story')

articles_reuters = [
	['title', 'text', 'url', 'picture', 'date', 'www.reuters.com'],
	['title', 'text', 'url', 'picture', 'date', 'www.reuters.com'],
	['title', 'text', 'url', 'picture', 'date', 'www.reuters.com'],
	['title', 'text', 'url', 'picture', 'date', 'www.reuters.com'],
	['title', 'text', 'url', 'picture', 'date', 'www.reuters.com'],#5
	['title', 'text', 'url', 'picture', 'date', 'www.reuters.com'],
	['title', 'text', 'url', 'picture', 'date', 'www.reuters.com'],
	['title', 'text', 'url', 'picture', 'date', 'www.reuters.com'],
	['title', 'text', 'url', 'picture', 'date', 'www.reuters.com'],
	['title', 'text', 'url', 'picture', 'date', 'www.reuters.com']#10
	]

for i in range(0,10):
	articles_reuters[i][0] = str(title_html_reuters[i]).split('>')[1].split('<')[0].strip()
	articles_reuters[i][1] = str(text_html_reuters[i]).split('<p>')[1].split('</p>')[0]
	articles_reuters[i][2] = 'https://www.reuters.com' + str(url_html_reuters[i]).split('href="')[1].split('">')[0]
	articles_reuters[i][3] = 'https://i.ibb.co/n3fSDq7/placeholder.png'

	dte =  str(date_html_reuters[i]).split('timestamp">')[1].split('<')[0]
	try:
		articles_reuters[i][4] = datetime.strptime(dte, '%d %b %Y').strftime('%Y-%m-%d')
	except:
		articles_reuters[i][4] = str(datetime.today().date())


url = 'https://uk.reuters.com/subjects/aerospace-and-defence'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
pics_html_reuters = soup.find_all(class_='story')
for i in range(0,10):
	try:
		articles_reuters[i][3] = str(pics_html_reuters[i]).split('org-src="')[1].split('"')[0].replace('amp;', '')
	except:
		articles_reuters[i][3] = 'https://i.ibb.co/n3fSDq7/placeholder.png'

articles_reuters = articles_reuters[1::]

#print(str(date_html_reuters[1]).split('timestamp">')[1].split('<')[0])
