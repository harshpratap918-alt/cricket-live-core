from flask import Flask, render_template
import requests

app = Flask(__name__)

# Aapki RapidAPI Details
RAPID_API_KEY = "c83e887053mshb3e304f84916276p1e8976jsn4ead0beaafab"
RAPID_API_HOST = "free-cricbuzz-cricket-api.p.rapidapi.com"

@app.route('/')
def index():
    url = f"https://{RAPID_API_HOST}/matches/list"
    headers = {
        "X-RapidAPI-Key": RAPID_API_KEY,
        "X-RapidAPI-Host": RAPID_API_HOST
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        data = response.json()
        match_list = data.get('matchList', [])
        
        if match_list:
            # Live match dhoondhna, nahi toh pehla match lena
            live_match = next((m for m in match_list if m.get('state') == 'live'), match_list[0])
            
            match_info = {
                "title": live_match.get("seriesName", "Core Sports News"),
                "status": live_match.get("status", "Match Information Updating..."),
                "score": f"{live_match.get('matchDesc', '')} {live_match.get('matchFormat', '')}"
            }
        else:
            match_info = {
                "title": "Core Sports",
                "status": "Abhi koi live match nahi hai",
                "score": "Naye match ka intezaar karein"
            }
            
    except Exception as e:
        match_info = {
            "title": "Core Sports Live",
            "status": "Stadium se connect ho raha hai...",
            "score": "Please Refresh"
        }

    return render_template('index.html', match=match_info)

if __name__ == '__main__':
    app.run(debug=True)