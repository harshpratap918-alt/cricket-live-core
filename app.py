from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    # Default information
    match_info = {
        "title": "Core Sports News",
        "status": "Live Match Updating...",
        "score": "Please Refresh"
    }
    
    try:
        url = "https://free-cricbuzz-cricket-api.p.rapidapi.com/matches/list"
        headers = {
            "X-RapidAPI-Key": "c83e887053mshb3e304f84916276p1e8976jsn4ead0beaafab",
            "X-RapidAPI-Host": "free-cricbuzz-cricket-api.p.rapidapi.com"
        }
        # Timeout ko 5 second rakha hai taaki crash na ho
        response = requests.get(url, headers=headers, timeout=5)
        
        if response.status_code == 200:
            data = response.json()
            m_list = data.get('matchList', [])
            if m_list:
                m = m_list[0]
                match_info["title"] = str(m.get("seriesName", "Core Sports"))
                match_info["status"] = str(m.get("status", "Live"))
                match_info["score"] = str(m.get("matchDesc", "Score Updating"))
    except Exception as e:
        print(f"Error: {e}")

    return render_template('index.html', match=match_info)

if __name__ == '__main__':
    app.run()
