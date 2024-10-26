import matching_system

from dotenv import load_dotenv
from flask import Flask, render_template, request
import os

load_dotenv()

app = Flask(__name__)

api_url = ""

@app.route('/')
def index():
    api_key = os.getenv('GOOGLE_MAPS_API_KEY')
    api_url = f"https://maps.googleapis.com/maps/api/js?key={api_key}&callback=initMap"
    return render_template('index.html', api_url=api_url)

@app.route('/about.html')
def about():
    api_key = os.getenv('GOOGLE_MAPS_API_KEY')
    api_url = f"https://maps.googleapis.com/maps/api/js?key={api_key}&callback=initMap"
    return render_template('about.html', api_url=api_url)

@app.route('/createAccount.html')
def createAccount():
    api_key = os.getenv('GOOGLE_MAPS_API_KEY')
    api_url = f"https://maps.googleapis.com/maps/api/js?key={api_key}&callback=initMap"
    return render_template('createAccount.html', api_url=api_url)

@app.route('/home.html')
def home():
    api_key = os.getenv('GOOGLE_MAPS_API_KEY')
    api_url = f"https://maps.googleapis.com/maps/api/js?key={api_key}&callback=initMap"
    return render_template('home.html', api_url=api_url)

@app.route('/map.html')
def map():
    global api_url
    api_key = os.getenv('GOOGLE_MAPS_API_KEY')
    api_url = f"https://maps.googleapis.com/maps/api/js?key={api_key}&callback=initMap"
    return render_template('map.html', api_url=api_url, names=None)

@app.route('/match', methods=['POST'])
def match():
    # Get the info from the form
    address = request.form['address']
    radius = int(request.form['radius'])
    
    # Find distributors
    users = matching_system.find_distributors_radius(address, radius)
    names = [user['location'] for user in users]

    global api_url

    # Render the HTML with the result
    return render_template('map.html', api_url=api_url, names=names)

if __name__ == '__main__':
    app.run(debug=True)
