# app.py
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World! Welcome to the Flask App!'

if __name__ == '__main__':
    app.run(debug=True)