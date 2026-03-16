from flask import Flask, render_template
import requests
import os

app = Flask(__name__)

# Cricket Data
def get_cricket():
    url = "https://cricbuzz-cricket.p.rapidapi.com/matches/v1/recent"
    headers = {
        "X-RapidAPI-Key": "c83e887053mshb3e304f84916276p1e8976jsn4ead0beaafab",
        "X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com"
    }
    try:
        r = requests.get(url, headers=headers, timeout=5)
        return r.json().get('typeMatches', [])
    except:
        return []

@app.route('/')
def index():
    cricket = get_cricket()
    # Football aur NBA data yahan connect hoga
    return render_template('index.html', cricket=cricket)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
