from flask import Flask, jsonify, request, render_template
from datetime import datetime
from snack_data import get_snacks_by_mood_and_time

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def suggest_snack():
    if request.method == 'POST':
        mood = request.form.get('mood')
        time = request.form.get('time')

        if not mood or not time:
            return "Please provide both mood and time", 400

        suggestions = get_snacks_by_mood_and_time(mood.lower(), time.lower())
        response_text = "<h3>Suggest Snacks:</h3><br>" + "<br>".join(suggestions)
        return response_text, 200

    return render_template('suggest_form.html')


@app.route('/about', methods=['GET'])
def about():
    return jsonify({
        "project": "Have Healthy Snacks API",
        "developer": "Abhijeet Kamthe"
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
