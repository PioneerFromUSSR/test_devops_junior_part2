# app.py
from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/greet')
def greet():
    return render_template('greet.html')

# Omittable
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)