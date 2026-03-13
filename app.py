from flask import Flask, render_template
import requests
import os

app = Flask(__name__)

def get_cricket_data():
    url = "https://cricbuzz-cricket.p.rapidapi.com/matches/v1/recent"
    headers = {
        "X-RapidAPI-Key": "c83e887053mshb3e304f84916276p1e8976jsn4ead0beaafab",
        "X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com"
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        return response.json().get('typeMatches', [])
    except Exception:
        return []

@app.route('/')
def index():
    matches = get_cricket_data()
    return render_template('index.html', matches=matches)

if __name__ == "__main__":
    # Render automatically uses the PORT environment variable
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
