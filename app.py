from flask import Flask, render_template
import requests
import feedparser
import os

app = Flask(__name__)

# RapidAPI Headers (Aapki Key ke saath)
HEADERS = {
    "X-RapidAPI-Key": "c83e887053mshb3e304f84916276p1e8976jsn4ead0beaafab",
    "X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com"
}

def get_cricket():
    try:
        url = "https://cricbuzz-cricket.p.rapidapi.com/matches/v1/recent"
        r = requests.get(url, headers=HEADERS, timeout=5)
        return r.json().get('typeMatches', [])
    except: return []

def get_news(sport_type):
    # RSS Feeds for Automation
    feeds = {
        'cricket': "https://www.espn.com/espn/rss/cricket/news",
        'football': "https://www.espn.com/espn/rss/football/news",
        'nba': "https://www.espn.com/espn/rss/nba/news"
    }
    try:
        feed = feedparser.parse(feeds.get(sport_type))
        return feed.entries[:5] # Top 5 headlines
    except: return []

@app.route('/')
def index():
    data = {
        'cricket_scores': get_cricket(),
        'cricket_news': get_news('cricket'),
        'football_news': get_news('football'),
        'nba_news': get_news('nba')
    }
    return render_template('index.html', **data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
