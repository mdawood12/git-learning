import requests

def get_weather_openmeteo():
    """Get weather using Open-Meteo (no API key required)"""
    url = 'https://api.open-meteo.com/v1/forecast'
    
    # Parameters for your location
    params = {
        'latitude': 34.01,  # Change to your city's latitude
        'longitude': 71.58,  # Change to your city's longitude
        'current_weather': True,
        'hourly': 'temperature_2m,relativehumidity_2m,windspeed_10m',
        'timezone': 'auto'
    }
    
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        # Current weather
        current = data['current_weather']
        print("\n🌤️ CURRENT WEATHER")
        print(f"Temperature: {current['temperature']}°C")
        print(f"Wind Speed: {current['windspeed']} km/h")
        print(f"Wind Direction: {current['winddirection']}°")
        
        # Hourly forecast
        hourly = data['hourly']
        print("\n📊 NEXT 6 HOURS FORECAST")
        for i in range(6):
            print(f"Hour {i+1}: {hourly['temperature_2m'][i]}°C, "
                  f"{hourly['relativehumidity_2m'][i]}% humidity")
                  
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    except KeyError as e:
        print(f"Data parsing error: {e}")

if __name__ == "__main__":
    get_weather_openmeteo()