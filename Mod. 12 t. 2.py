# Tutustu avoimeen OpenWeather-säärajapintaan: https://openweathermap.org/api.
# Kirjoita ohjelma, joka kysyy käyttäjältä paikkakunnan nimen ja tulostaa sitä
# vastaavan säätilan tekstin sekä lämpötilan Celsius-asteina.
# Perehdy rajapinnan dokumentaatioon riittävästi. Palveluun rekisteröityminen on tarpeen,
# jotta saat rajapintapyynnöissä tarvittavan API-avaimen (API key).
# Selvitä myös, miten saat Kelvin-asteet muunnettua Celsius-asteiksi.


import requests


base_url = "https://api.openweathermap.org/data/2.5/weather?"
api_avain = "e76965d853e439fea2c006d1e2545908"
city = input("Enter city name: ")

url = base_url + "appid=" + api_avain + "&q=" + city + "&units=metric&lang=fi"

try:
    response = requests.get(url)
    if response.status_code == 200:
        json_response = response.json()
        temp = json_response['main']['temp']
        description = json_response['weather'][0]['description']
        country = json_response['sys']['country']
        print(f"{country}\n"
              f"{city}\n"
              f"Temperature: {temp}°C\n"
              f"Weather: {description}")
    elif response.status_code == 404:
        print(f"City: {city}, not found error 404.")

except requests.exceptions.RequestException as e:
    print("Your search cannot be performed." + str(e))