from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    # Emergency Backup Data
    match_info = {
        "title": "Core Sports News",
        "status": "Live Scores Updating...",
        "score": "Please Refresh in a moment"
    }
    
    # Sirf ye 4 lines check karega, agar error aaya toh seedha match_info dikhayega
    try:
        url = "https://free-cricbuzz-cricket-api.p.rapidapi.com/matches/list"
        headers = {
            "X-RapidAPI-Key": "c83e887053mshb3e304f84916276p1e8976jsn4ead0beaafab",
            "X-RapidAPI-Host": "free-cricbuzz-cricket-api.p.rapidapi.com"
        }
        response = requests.get(url, headers=headers, timeout=5)
        if response.status_code == 200:
            data = response.json()
            m_list = data.get('matchList', [])
            if m_list:
                m = m_list[0]
                match_info["title"] = m.get("seriesName", "Core Sports")
                match_info["status"] = m.get("status", "Live")
                match_info["score"] = f"{m.get('matchDesc', '')}"
    except:
        pass # Error aane par bhi website crash nahi hogi

    return render_template('index.html', match=match_info)

if __name__ == '__main__':
    app.run(debug=True)
