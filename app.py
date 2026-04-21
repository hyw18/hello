from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    skills = [
        "C", "C++", "C#", "Java", "Kotlin"
    ]
    return render_template('index.html', data=skills)

@app.route('/send', methods=['POST'])
def send():
    skill = request.form.get('skill')
    level = request.form.get('level')
    return skill + " " + level

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
