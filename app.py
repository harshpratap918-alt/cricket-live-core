from flask import Flask, render_template
import requests

app = Flask(__name__)

def get_live_data():
    try:
        url = "https://cricket-api-unofficial.vercel.app/live"
        response = requests.get(url, timeout=10)
        data = response.json()
        if data.get('status') == 'success':
            return data.get('matches', [])
        return []
    except:
        return []

@app.route('/')
def index():
    matches = get_live_data()
    return render_template('index.html', matches=matches)

if __name__ == '__main__':
    app.run()
