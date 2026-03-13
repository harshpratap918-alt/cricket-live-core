from flask import Flask, render_template
import requests
import os

app = Flask(__name__)

def get_cricket_data():
    # Cricbuzz API URL aur Headers
    url = "https://cricbuzz-cricket.p.rapidapi.com/matches/v1/recent"
    headers = {
        "X-RapidAPI-Key": "c83e887053mshb3e304f84916276p1e8976jsn4ead0beaafab",
        "X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com"
    }
    try:
        response = requests.get(url, headers=headers, timeout=15)
        if response.status_code == 200:
            data = response.json()
            # Cricbuzz API ka structure 'typeMatches' hota hai
            return data.get('typeMatches', [])
        return []
    except Exception as e:
        print(f"API Error: {e}")
        return []

@app.route('/')
def index():
    matches = get_cricket_data()
    return render_template('index.html', matches=matches)

@app.route('/highlights')
def highlights():
    return render_template('highlights.html')

if __name__ == '__main__':
    # Render ke liye zaroori port configuration
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
