from flask import Flask, render_template, request, redirect, url_for
import requests, os, datetime
from dotenv import load_dotenv
from app.data.response_items import get_image, get_explanation



load_dotenv() 

API_KEY = os.getenv("API_KEY")
image_of_the_day_url = 'https://api.nasa.gov/planetary/apod?api_key={}'
response = requests.get(image_of_the_day_url.format(API_KEY)) 

app = Flask(__name__)

@app.route('/')
def index():

    image = get_image(response)
    image_description = get_explanation(response)
    
    return render_template('index.html', landing_image=image, explanation=image_description)

@app.route('/mars')
def mars():
    return render_template('mars.html')

print(API_KEY)
print(response.json())
print(response.json()["url"])
print(response.json()["explanation"])

