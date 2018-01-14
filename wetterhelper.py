import feedparser

Wetter = "http://www.br.de/wetter/action/feeds/bayernwetter.do"


class Unterfranken():

    def __init__(self, url=Wetter):

        self.URL = url
        self.Wetter_news = []

    def get_Weather(self):

        
        feed = feedparser.parse(self.URL)
	article = feed['entries']

	for i in range(7):

            self.Wetter_news.append(article[i]['summary_detail']['value'])

	

	return self.Wetter_news


