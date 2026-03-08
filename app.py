from flask import Flask, render_template
import requests
import os

app = Flask(__name__)

def get_scores():
    try:
        # Stable API URL
        url = "https://cricket-api-unofficial.vercel.app/live"
        # Timeout ko 15 second kar diya hai taaki slow net pe crash na ho
        response = requests.get(url, timeout=15)
        if response.status_code == 200:
            data = response.json()
            return data.get('matches', [])
        return []
    except Exception as e:
        print(f"Connection Error: {e}")
        return []

@app.route('/')
def index():
    matches = get_scores()
    return render_template('index.html', matches=matches)

if __name__ == '__main__':
    # Render ke liye port set karna zaruri hai
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
