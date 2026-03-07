from flask import Flask, render_template
import requests

app = Flask(__name__)

# Ye rahi aapki key jo photo mein dikh rahi hai
RAPID_API_KEY = "c83e887053mshb3e304f84916276p1e8976jsn4ead0beaafab"
RAPID_API_HOST = "free-cricbuzz-cricket-api.p.rapidapi.com"

@app.route('/')
def index():
    # Asli live match data mangne ke liye URL
    url = f"https://{RAPID_API_HOST}/matches/list"
    headers = {
        "X-RapidAPI-Key": RAPID_API_KEY,
        "X-RapidAPI-Host": RAPID_API_HOST
    }
    
    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        
        # Sabse pehla live match uthayenge
        match_list = data.get('matchList', [])
        live_match = next((m for m in match_list if m.get('state') == 'live'), match_list[0])
        
        match_info = {
            "title": live_match.get("seriesName", "Core Sports Live"),
            "status": live_match.get("status", "Match Updating..."),
            "score": f"{live_match.get('matchDesc', '')} - {live_match.get('matchFormat', '')}"
        }
    except:
        match_info = {
            "title": "Core Sports Live",
            "status": "Stadium se connect ho raha hai...",
            "score": "Please Wait"
        }

    return render_template('index.html', match=match_info)

if __name__ == '__main__':
    app.run(debug=True)