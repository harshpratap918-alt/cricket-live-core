from flask import Flask, render_template
import requests

app = Flask(__name__)

def get_cricket_data():
    try:
        # 'all' endpoint se live aur purane dono matches milte hain
        url = "https://cricket-api-unofficial.vercel.app/all"
        response = requests.get(url, timeout=10)
        data = response.json()
        
        if data.get('status') == 'success':
            matches = data.get('matches', [])
            live_matches = [m for m in matches if m['status'] == 'live']
            # Pichle 5 matches ka status nikalna
            old_matches = [m for m in matches if m['status'] == 'completed'][:5]
            return live_matches, old_matches
        return [], []
    except:
        return [], []

@app.route('/')
def index():
    live, old = get_cricket_data()
    return render_template('index.html', live_matches=live, old_matches=old)

if __name__ == '__main__':
    app.run()
