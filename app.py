from flask import Flask, render_template, request
from utils.weather import get_weather
from utils.fashion import suggest_outfits
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/style', methods=['POST'])
def style():
    destination = request.form.get('destination', '')
    travel_date = request.form.get('travel_date', '')
    budget = request.form.get('budget', '')

    weather_info = get_weather(destination, travel_date)
    outfits = suggest_outfits(weather_info, budget)

    return render_template('results.html', destination=destination, travel_date=travel_date,
                           weather=weather_info, outfits=outfits)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
