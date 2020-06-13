from flask import Flask, render_template
from getting_article_aeromag import articles_aeromag
from getting_article_spacenews import articles_spacenews
from getting_article_from_ainonline import articles_aironline
from getting_article_reuters import articles_reuters
from getting_article_ukaviation import articles_ukaviation
from datetime import datetime

app = Flask(__name__)

articles = articles_aeromag + articles_spacenews + articles_aironline + articles_reuters + articles_ukaviation
articles = articles_aeromag + articles_spacenews + articles_aironline + articles_ukaviation
articles = articles_spacenews + articles_aeromag + articles_ukaviation + articles_reuters + articles_aironline
articles = articles_aeromag
articles = articles_spacenews + articles_aironline + articles_reuters + articles_ukaviation


print(articles)
dates = []
for line in articles:
	dates.append(line[4])

articles = sorted(articles, key=lambda x: datetime.strptime(x[4], '%Y-%m-%d'))


articles = articles[::-1]





index_del = []
for i in range(0, len(articles)):
	if articles[i][3] == 'https://i.ibb.co/n3fSDq7/placeholder.png':
		del articles[i][:]
		index_del.append(i)

for i in index_del:
	del articles[i]

articles = [x for x in articles if x]

@app.route('/')
def home():
	return render_template('index.html', articles=articles)

if __name__ == '__main__':
	app.run()

''' //TODO
- make everything responsive ie everything in the middle of screen
- add another element on the side, maybe elon tweets, videos
'''

# ain tells ukaviation to go away

