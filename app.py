from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    try:
        # Kal ke match ke liye hum yahan asli API link daalenge
        # Abhi ke liye ye internet check karne ke liye dummy data hai
        match_data = {
            "teams": "IND vs NZ (Tomorrow)",
            "score": "Match starts at 9:30 AM",
            "overs": "0.0",
            "status": "Ready for Live Action!"
        }
    except Exception as e:
        match_data = {
            "teams": "Error",
            "score": "Internet Connection Check Karein",
            "overs": "-",
            "status": str(e)
        }
    
    return render_template('index.html', data=match_data)

if __name__ == "__main__":
    app.run(debug=True)