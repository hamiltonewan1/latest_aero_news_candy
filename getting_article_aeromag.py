import requests
from bs4 import BeautifulSoup

url = 'https://www.aero-mag.com/category/news/'

page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

titles_html_aeromag = soup.find_all(class_='tile-title', itemprop='headline')
texts_html_aeromag = soup.find_all(class_='tile-description', itemprop='description')
urls_html_aeromag= soup.find_all(itemprop='mainEntityOfPage')
pics_html_aeromag = soup.find_all('img')
dates_html_aeromag = soup.find_all(itemprop='datePublished')


articles_aeromag = [
	['title', 'text', 'url', 'picture', 'date', 'www.aero-mag.com'],
	['title', 'text', 'url', 'picture', 'date', 'www.aero-mag.com'],
	['title', 'text', 'url', 'picture', 'date', 'www.aero-mag.com'],
	['title', 'text', 'url', 'picture', 'date', 'www.aero-mag.com'],
	['title', 'text', 'url', 'picture', 'date', 'www.aero-mag.com'],#5
	['title', 'text', 'url', 'picture', 'date', 'www.aero-mag.com'],
	['title', 'text', 'url', 'picture', 'date', 'www.aero-mag.com'],
	['title', 'text', 'url', 'picture', 'date', 'www.aero-mag.com'],
	['title', 'text', 'url', 'picture', 'date', 'www.aero-mag.com'],
	['title', 'text', 'url', 'picture', 'date', 'www.aero-mag.com']]
	
	

for i in range(0,10):
	articles_aeromag[i][0] = titles_html_aeromag[i].get_text().strip()
	articles_aeromag[i][1] = texts_html_aeromag[i].get_text().strip()
	articles_aeromag[i][2] = str(urls_html_aeromag[i]).split('"')[1]
	articles_aeromag[i][3] = str(pics_html_aeromag[i+2]).split('"')[3]
	articles_aeromag[i][4] = str(dates_html_aeromag[i]).split('"')[1].split('T')[0]



