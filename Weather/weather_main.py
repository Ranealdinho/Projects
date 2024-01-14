import requests

def get_weather(city):
    # API endpoint URL
    url = f"https://www.metaweather.com/api/location/search/?query={city}"
    
    try:
        # Send GET request to the API
        response = requests.get(url)
        data = response.json()
        
        if data:
            woeid = data[0]["woeid"]
            
            # API endpoint URL for weather data
            weather_url = f"https://www.metaweather.com/api/location/{woeid}/"
            
            # Send GET request to the weather data API
            weather_response = requests.get(weather_url)
            weather_data = weather_response.json()
            
            # Extract relevant weather information
            consolidated_weather = weather_data["consolidated_weather"][0]
            
            weather = {
                "city": city,
                "weather_state": consolidated_weather["weather_state_name"],
                "temperature": consolidated_weather["the_temp"],
                "humidity": consolidated_weather["humidity"],
                "wind_speed": consolidated_weather["wind_speed"]
            }
            
            return weather
        else:
            print("City not found.")
            return None
    
    except requests.exceptions.RequestException as e:
        print("Error occurred:", e)
        return None

# Main program
city = input("Enter a city name: ")
weather = get_weather(city)

if weather:
    print(f"Weather in {weather['city']}:")
    print("Weather State:", weather["weather_state"])
    print("Temperature:", weather["temperature"])
    print("Humidity:", weather["humidity"])
    print("Wind Speed:", weather["wind_speed"])
else:
    print("Failed to fetch weather data.")