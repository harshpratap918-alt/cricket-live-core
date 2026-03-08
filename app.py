from flask import Flask, render_template
import requests

app = Flask(__name__)

def get_live_scores():
    try:
        # Stable public API for live cricket
        url = "https://cricket-api-unofficial.vercel.app/live"
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            return data.get('matches', [])
        return []
    except:
        return []

@app.route('/')
def index():
    matches = get_live_scores()
    return render_template('index.html', matches=matches)

if __name__ == '__main__':
    app.run(debug=True)

