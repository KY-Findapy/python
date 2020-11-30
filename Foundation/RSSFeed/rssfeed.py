import feedparser
feed = feedparser.parse('https://news.un.org/feed/subscribe/en/news/topic/economic-development/feed/rss.xml')
type(feed)
dir(feed)
feed.href
len(feed.entries)
feed.entries[0]
print(feed.entries[0].title)
