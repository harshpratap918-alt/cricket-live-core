from flask import Flask, render_template
import requests
import feedparser # Nayi library news ke liye
import os

app = Flask(__name__)

def get_cricket():
    # Aapka purana cricket API logic
    url = "https://cricbuzz-cricket.p.rapidapi.com/matches/v1/recent"
    headers = {"X-RapidAPI-Key": "YOUR_KEY", "X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com"}
    try:
        r = requests.get(url, headers=headers, timeout=5)
        return r.json().get('typeMatches', [])
    except: return []

def get_news():
    # Yeh automatically ESPN ki news uthayega
    feed_url = "https://www.espn.com/espn/rss/cricket/news"
    feed = feedparser.parse(feed_url)
    return feed.entries[:5] # Top 5 headlines

@app.route('/')
def index():
    cricket = get_cricket()
    news = get_news()
    return render_template('index.html', cricket=cricket, news=news)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
