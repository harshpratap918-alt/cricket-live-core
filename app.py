from flask import Flask, render_template
from pycricbuzz import Cricbuzz

app = Flask(__name__)
c = Cricbuzz()

def get_live_match_data():
    try:
        all_matches = c.matches()
        # Hum saare matches check karenge jo abhi chal rahe hain
        for match in all_matches:
            # Agar match live hai, ya break chal raha hai, ya stumps hue hain
            if match['mchstate'] in ['live', 'innings break', 'lunch', 'tea', 'stumps', 'toss']:
                return {
                    'title': f"{match['team1']['name']} vs {match['team2']['name']}",
                    'format': match['type'],
                    'score': match.get('status', 'Score Updating...'),
                    'full_status': f"Match State: {match['mchstate'].upper()}"
                }
        
        # Agar koi match live nahi hai toh aakhri khatam hua match dikhao
        return {
            'title': "No Live Match Currently",
            'format': "Core Sports News",
            'score': "Next match starting soon!",
            'full_status': "Stay tuned for updates"
        }
    except Exception as e:
        return {
            'title': "Network Busy",
            'format': "Error",
            'score': "Please refresh the page",
            'full_status': str(e)
        }

@app.route('/')
def index():
    match_info = get_live_match_data()
    return render_template('index.html', match=match_info)

if __name__ == '__main__':
    app.run(debug=True)
