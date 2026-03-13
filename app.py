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
        response = requests.get(url, headers=headers, timeout=15)
        if response.status_code == 200:
            return response.json().get('typeMatches', [])
        return []
    except:
        return []

@app.route('/')
def index():
    matches = get_cricket_data()
    return render_template('index.html', matches=matches)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
