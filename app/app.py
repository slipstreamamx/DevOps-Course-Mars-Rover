from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', landing_image='https://via.placeholder.com/500')

@app.route('/mars')
def mars():
    return render_template('mars.html')