from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    city = request.args.get('city')
    weather = None
    forecast = []

    if city:
        api_key = '069ffabe4810b705c570534f6a2acc73'
        weather_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid={api_key}'
        forecast_url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&units=imperial&appid={api_key}'

        weather_data = requests.get(weather_url).json()
        forecast_data = requests.get(forecast_url).json()

        if weather_data.get('main'):
            weather = {
                'temp': weather_data['main']['temp'],
                'description': weather_data['weather'][0]['description'],
                'humidity': weather_data['main']['humidity'],
            }

        if forecast_data.get('list'):
            for item in forecast_data['list']:
                forecast.append({
                    'date': item['dt_txt'].split(' ')[0],
                    'temp': item['main']['temp'],
                    'description': item['weather'][0]['description'],
                })
                if len(forecast) >= 5:  # Limit to 5 days
                    break

    return render_template('index.html', weather=weather, city=city, forecast=forecast)

if __name__ == "__main__":
    app.run(debug=True, port=5001)


