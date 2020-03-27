import feedparser

RSS_URL = "https://b.hatena.ne.jp/hotentry/it.rss"

d = feedparser.parse(RSS_URL)
for entry in d.entries[:3]:
    print(entry.title, entry.link)
