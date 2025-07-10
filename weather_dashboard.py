import requests
import matplotlib.pyplot as plt

# Replace with your actual API key from OpenWeatherMap
API_KEY = '519bf1da95ab6283c6dfe4b2f9f3368c'
CITY = 'Bangalore'

URL = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

# Fetch weather data
response = requests.get(URL)
data = response.json()

# Print data to debug
print(data)

# Check for errors
if data.get("cod") != "200":
    print("❌ Error fetching data:", data.get("message"))
else:
    dates = []
    temperatures = []
    humidities = []

    # Only show first 8 records (24 hours)
    for forecast in data['list'][:8]:
        dates.append(forecast['dt_txt'])
        temperatures.append(forecast['main']['temp'])
        humidities.append(forecast['main']['humidity'])

    # Plot the data
    plt.figure(figsize=(12, 6))
    plt.plot(dates, temperatures, label='Temperature (°C)', marker='o')
    plt.plot(dates, humidities, label='Humidity (%)', marker='x')
    plt.xticks(rotation=45)
    plt.title(f"Weather Forecast for {CITY} (Next 24 Hours)")
    plt.xlabel("Date & Time")
    plt.ylabel("Values")
    plt.legend()
    plt.tight_layout()
    plt.grid()
    plt.show()
