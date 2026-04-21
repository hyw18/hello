from flask import Flask, render_template, request, redirect

app = Flask(__name__)
messages = []

@app.route('/')
def home():
    skill = [
        "C", "C++", "C#", "Java",
        "JavaScript",
        "Python"
    ]
    return render_template('index.html', data=skill, messages=messages)

@app.route('/send', methods=['POST'])
def send():
    skill = request.form.get('skill')
    level = request.form.get('level')
    messages.append(skill + " / " + level)
    return redirect('/')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
