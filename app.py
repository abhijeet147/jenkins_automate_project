from flask import Flask, jsonify, request
from datetime import datetime
from snack_data import get_snacks_by_mood_and_time

app = Flask(__name__)

@app.route('/home')
  return ("WELCOME TO HAVE HEALTHY SNACKS API !!!")


@app.route('/about', methods=['GET'])
def about():
    return jsonify({"project": "Have Healthy Snacks API",
                    "developer": "Abhijeet Kamthe"})


@app.route('/suggest', methods=['GET'])
def suggest_snack():
    mood = request.args.get('mood')
    hour = datetime.now().hour
    time_of_day = (
        'morning' if 5 <= hour < 12 else
        'afternoon' if 12 <= hour < 17 else
        'evening' if 17 <= hour < 21 else
        'night'
    )
    suggestions = get_snacks_by_mood_and_time(mood, time_of_day)
    return jsonify({
        "time_of_day": time_of_day,
        "mood": mood,
        "suggestions": suggestions
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)






