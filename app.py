from flask import Flask, render_template
import requests
import os

app = Flask(__name__)

def get_live_scores():
    try:
        # Stable Cricket API
        url = "https://cricket-api-unofficial.vercel.app/live"
        response = requests.get(url, timeout=12)
        if response.status_code == 200:
            data = response.json()
            if data.get('status') == 'success':
                return data.get('matches', [])
        return []
    except:
        return []

@app.route('/')
def index():
    matches = get_live_scores()
    return render_template('index.html', matches=matches)

if __name__ == '__main__':
    # Render ke liye dynamic port binding
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
