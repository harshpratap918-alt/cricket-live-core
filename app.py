from flask import Flask, render_template, url_for
import requests
import feedparser

app = Flask(__name__)

# Cricket API with Timeout
def get_cricket():
    url = "https://cricbuzz-cricket.p.rapidapi.com/matches/v1/recent"
    headers = {
        "X-RapidAPI-Key": "YOUR_ACTUAL_API_KEY", # Apni key yahan check karein
        "X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com"
    }
    try:
        # Timeout=5 lagane se site hang nahi hogi
        response = requests.get(url, headers=headers, timeout=5)
        if response.status_code == 200:
            return response.json().get('typeMatches', [])
        return []
    except Exception as e:
        print(f"Cricket API Error: {e}")
        return []

# News RSS with Timeout
def get_news(sport):
    feeds = {
        'cricket': "https://www.espn.com/espn/rss/cricket/news",
        'football': "https://www.espn.com/espn/rss/football/news"
    }
    try:
        feed = feedparser.parse(feeds.get(sport))
        return feed.entries[:5]
    except:
        return []

@app.route('/')
def index():
    cricket_data = get_cricket()
    news_data = get_news('cricket')
    return render_template('index.html', cricket=cricket_data, c_news=news_data)

if __name__ == "__main__":
    app.run(debug=True)
