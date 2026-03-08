from flask import Flask, render_template
import requests

app = Flask(__name__)

def get_scores():
    # Source 1: Main API
    urls = [
        "https://cricket-api-unofficial.vercel.app/live",
        "https://api.cricapi.com/v1/currentMatches?apikey=YOUR_FREE_KEY&offset=0" # Backup (Optional)
    ]
    
    for url in urls:
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                data = response.json()
                if data.get('status') == 'success' and data.get('matches'):
                    return data['matches']
        except:
            continue
    return []

@app.route('/')
def index():
    matches = get_scores()
    return render_template('index.html', matches=matches)

if __name__ == '__main__':
    app.run()
