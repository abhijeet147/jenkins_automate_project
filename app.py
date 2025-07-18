from flask import Flask, jsonify, request ,render_template
from datetime import datetime
from snack_data import get_snacks_by_mood_and_time

app = Flask(__name__)

@app.route('/', methods = ['GET','POST'])
def suggest_snack():
    
    if request.method == 'POST':
        mood = request.form['mood']
        time = request.form['time']
        
        suggestions = get_snacks_by_mood_and_time(mood.lower(), time.lower())

        return jsonify({
            'Mood': mood,
            'Time': time,
            'Suggested Snack': suggestions
        })
    return render_template('suggest_form.html')

    


@app.route('/about', methods=['GET'])
def about():
    return jsonify({"project": "Have Healthy Snacks API",
                    "developer": "Abhijeet Kamthe"})



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000 ,debug=True)






