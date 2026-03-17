from flask import Flask, render_template
import requests
import feedparser

app = Flask(__name__)

# Aapki provided RapidAPI Key yahan set hai
RAPID_API_KEY = "c83e887053mshb3e304f84916276p1e8976jsn4ead0beaafab"

def get_cricket():
    url = "https://cricbuzz-cricket.p.rapidapi.com/matches/v1/recent"
    headers = {
        "X-RapidAPI-Key": RAPID_API_KEY,
        "X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com"
    }
    try:
        # Timeout=5 takki API slow ho toh site hang na ho
        response = requests.get(url, headers=headers, timeout=5)
        if response.status_code == 200:
            return response.json().get('typeMatches', [])
        return []
    except Exception as e:
        print(f"Error fetching cricket data: {e}")
        return []

def get_news():
    try:
        # Sports news feed
        feed = feedparser.parse("https://www.espn.com/espn/rss/cricket/news")
        return feed.entries[:6]
    except:
        return []

@app.route('/')
def index():
    cricket_data = get_cricket()
    news_data = get_news()
    return render_template('index.html', cricket=cricket_data, news=news_data)

if __name__ == "__main__":
    app.run(debug=True)
