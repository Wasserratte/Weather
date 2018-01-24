import feedparser

br_feed = "https://www.br.de/nachrichten/aktuell-100~rss.xml"

class News_Feed():

    def get_news(self):

        feed = feedparser.parse(br_feed)
        article = feed['entries']
        return article



#br = News_Feed()

#news_feed = br.get_news()



#for article in news_feed:

 #   print article['link']
  #  print article['title']
   # print article['summary']
    #print article['updated']


