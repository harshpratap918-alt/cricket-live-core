from flask import Flask, render_template
import requests
import os

app = Flask(__name__)

# API Headers
HEADERS = {
    "X-RapidAPI-Key": "c83e887053mshb3e304f84916276p1e8976jsn4ead0beaafab",
    "X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com"
}

def get_cricket():
    try:
        url = "https://cricbuzz-cricket.p.rapidapi.com/matches/v1/recent"
        r = requests.get(url, headers=HEADERS, timeout=5)
        return r.json().get('typeMatches', [])
    except: return []

@app.route('/')
def index():
    cricket_data = get_cricket()
    # Football aur NBA ka data abhi placeholder rakha hai taaki site error na de
    return render_template('index.html', cricket=cricket_data)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
