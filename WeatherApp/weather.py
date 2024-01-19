import requests

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}  # You can change units to imperial for Fahrenheit

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            return data
        else:
            print(f"Error: {data['message']}")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def display_weather(weather_data):
    if weather_data:
        print("\nWeather Information:")
        print(f"City: {weather_data['name']}")
        print(f"Temperature: {weather_data['main']['temp']}°C")
        print(f"Description: {weather_data['weather'][0]['description']}")
        print(f"Humidity: {weather_data['main']['humidity']}%")
        print(f"Wind Speed: {weather_data['wind']['speed']} m/s")
    else:
        print("No weather information available.")

def main():
    api_key = 'fd03acc467ff3335f99af59968241c5e'  # Replace with your OpenWeatherMap API key

    while True:
        city = input("Enter the city name (or 'exit' to quit): ")

        if city.lower() == 'exit':
            print("Exiting the program. Goodbye!")
            break

        weather_data = get_weather(api_key, city)

        if weather_data:
            display_weather(weather_data)

if __name__ == "__main__":
    main()
