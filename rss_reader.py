import feedparser

def fetch_rss_feed(url):
    feed = feedparser.parse(url)
    return feed.entries

def display_feed(entries):
    for entry in entries:
        print("Title:", entry.title)
        print("Description:", entry.description)
        print("Link:", entry.link)
        print("\n")

if __name__ == "__main__":
    feed_url = input("Enter the RSS feed URL: ")
    entries = fetch_rss_feed(feed_url)
    display_feed(entries)
