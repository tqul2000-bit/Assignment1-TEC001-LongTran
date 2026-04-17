import requests


def get_weather():
    api_key = "82e649a7d1736c014daa04fd6140d9f2"
    base_url = "https://api.openweathermap.org/data/2.5/weather"

    municipality = input("Enter the name of a municipality: ")

    params = {
        "q": municipality,
        "appid": api_key,
        "units": "metric"
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()

        data = response.json()

        description = data['weather'][0]['description']
        temp_celsius = data['main']['temp']
        temp_kelvin = float(temp_celsius) + 273.15
        print(f"\nWeather in {municipality.capitalize()}:")
        print(f"Condition: {description}")
        print(f"Temperature Celsius: {temp_celsius:.2f}°C")
        print(f"Temperature Kelvin: {temp_kelvin:.2f}K")

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.JSONDecodeError:
        print("Error: Received a non-JSON response from the server.")
        print(f"Raw Response: {response.text}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    get_weather()