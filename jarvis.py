
# This is a *very* basic bot to get the weather forecast from a free web API

# A real bot would process (parse) the raw json data and print just the
# desired parts in a more readable format

# In PyCharm terminal:
# pdm install
# pdm run jarvis

# import the installed library that you need to request data from webservers
import requests

# import the built-in library that you need to process json data
import json


# Url to get the 7 day forecast for NoHo
# Based on https://open-meteo.com/en/docs
api_url = "https://api.open-meteo.com/v1/forecast?latitude=34.17&longitude=-118.38&timezone=GMT&days=0&daily=temperature_2m_max,temperature_2m_min,sunrise,sunset,precipitation_sum&temperature_unit=fahrenheit&windspeed_unit=mph"


def main():
    print(f"The weather in NoHo is:")
    # Get the next week's weather from the API url
    weather = requests.get(api_url)
    # Pretty print the Json response
    print(json.dumps(weather.json(), indent=4))


if __name__ == "__main__":
    main()