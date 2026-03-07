from flask import Flask, render_template
import requests

app = Flask(__name__)

# Verified API Key and Host
RAPID_API_KEY = "c83e887053mshb3e304f84916276p1e8976jsn4ead0beaafab"
RAPID_API_HOST = "free-cricbuzz-cricket-api.p.rapidapi.com"

@app.route('/')
def index():
    url = f"https://{RAPID_API_HOST}/matches/list"
    headers = {
        "X-RapidAPI-Key": RAPID_API_KEY,
        "X-RapidAPI-Host": RAPID_API_HOST
    }
    
    # Backup data (Default)
    match_info = {
        "title": "Core Sports Live",
        "status": "Stadium se connect ho raha hai...",
        "score": "Please Refresh in 1 minute"
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            match_list = data.get('matchList', [])
            
            if match_list:
                # Sabse pehle live match dhoondhna
                m = next((match for match in match_list if match.get('state') == 'live'), match_list[0])
                
                match_info["title"] = m.get("seriesName", "Core Sports News")
                match_info["status"] = m.get("status", "Updating Scores...")
                match_info["score"] = f"{m.get('matchDesc', '')} {m.get('matchFormat', '')}"
            else:
                match_info["status"] = "Abhi koi Match nahi hai"
        else:
            match_info["status"] = "API Busy - Please Refresh"
            
    except Exception as e:
        match_info["status"] = "Core Sports: Connecting..."

    return render_template('index.html', match=match_info)

if __name__ == '__main__':
    app.run(debug=True)
