def create_weather_plot(city):
    api_key = "ea7001e8a20197e795db6fe1c0c7de87"  # Make sure to copy the key directly from OpenWeatherMap
    data = create_weather_plot(city, api_key)
    # ... rest of the code ...


'''
import requests

city_name= 'New Delhi'
API_Key = 'ea7001e8a20197e795db6fe1c0c7de87'
url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_Key}&units=metric'

response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print(data)'''