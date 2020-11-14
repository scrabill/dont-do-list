from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', data=[
        {'description': "Don't commit murder"},
        {'description': "Don't leave the fridge door open long"},
        {'description': "Don't wear white after Labor day"}
    ])