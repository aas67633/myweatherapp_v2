# Weather App

## Overview

This is a 5-day forecast weather app created with Flask that allows users to enter a city and view the current weather in Fahrenheit for the entire week as well as additional details describing the forecast. The app fetches weather data from an API and displays it on a web page.

## Features

- Enter a city name to get the current weather.
- Displays the temperature in Fahrenheit.
- Shows weather details including temperature, humidity, and weather description.
- Includes detailed 5-day forecast

## How to Run

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/aas67633/myweatherapp_v2.git

2. **Navigate to the Project Directory**
   After cloning the repository, navigate into the project directory by using the command:
   cd myweatherapp

3. **Create a Virtual Environment**
   python -m venv venv

4. **Activate the Virtual Environment**
   Windows: venv\Scripts\activate
   macOS/Linux: source venv/bin/activate

5. **Install the Required Dependencies**
   Install all the necessary Python packages from the requirements.txt file using:
   pip install -r requirements.txt

6. **Run the Flask App**
   Use python app.py and run the app through http://127.0.0.1:5001/
