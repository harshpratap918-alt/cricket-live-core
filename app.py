from flask import Flask, render_template
import requests

app = Flask(__name__)

# Hum direct API URL use karenge taaki library ka error na aaye
def get_score():
    try:
        # Ye ek free public cricket API hai
        response = requests.get("https://cricket-api-unofficial.vercel.app/live")
        data = response.json()
        
        if data['status'] == 'success' and len(data['matches']) > 0:
            # Sabse pehla live match uthao (Womens ho ya Mens)
            match = data['matches'][0]
            return {
                'title': match['title'],
                'score': match['current_score'],
                'status': match['status_text'],
                'format': "LIVE"
            }
        return {'title': "No Live Match", 'score': "Next match soon!", 'status': "Stay Tuned", 'format': "OFFLINE"}
    except:
        return {'title': "Updating...", 'score': "Please refresh", 'status': "Connecting to stadium...", 'format': "WAIT"}

@app.route('/')
def index():
    match_info = get_score()
    return render_template('index.html', match=match_info)

if __name__ == '__main__':
    app.run(debug=True)
