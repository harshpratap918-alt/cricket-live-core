from flask import Flask, render_template, url_for
import requests
import feedparser
import os

app = Flask(__name__)

# Cricket Data (API)
def get_cricket():
    url = "https://cricbuzz-cricket.p.rapidapi.com/matches/v1/recent"
    headers = {
        "X-RapidAPI-Key": "YOUR_KEY_HERE",
        "X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com"
    }
    try:
        return requests.get(url, headers=headers).json().get('typeMatches', [])
    except: return []

# Global News (RSS Automation)
def get_news(sport):
    feeds = {
        'cricket': "https://www.espn.com/espn/rss/cricket/news",
        'football': "https://www.espn.com/espn/rss/football/news",
        'nba': "https://www.espn.com/espn/rss/nba/news"
    }
    try:
        return feedparser.parse(feeds.get(sport)).entries[:5]
    except: return []

@app.route('/')
def index():
    return render_template('index.html', 
                           cricket=get_cricket(),
                           c_news=get_news('cricket'),
                           f_news=get_news('football'),
                           n_news=get_news('nba'))

if __name__ == "__main__":
    app.run(debug=True)
