import requests
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Function to fetch weather data
def fetch_weather_data(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&units=metric&appid={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None

# Parse the weather data
def parse_weather_data(data):
    timestamps = []
    temperatures = []
    
    for entry in data['list']:
        timestamps.append(entry['dt_txt'])
        temperatures.append(entry['main']['temp'])
    
    return pd.DataFrame({'Timestamp': timestamps, 'Temperature (°C)': temperatures})

# Plot the weather data
def plot_weather_data(df, city):
    sns.set(style="whitegrid")
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=df, x='Timestamp', y='Temperature (°C)', marker='o')
    plt.xticks(rotation=45)
    plt.title(f"Temperature Trend for {city}", fontsize=16)
    plt.xlabel("Timestamp", fontsize=12)
    plt.ylabel("Temperature (°C)", fontsize=12)
    plt.tight_layout()
    plt.show()

# Main script
if __name__ == "__main__":
    # Replace with your OpenWeatherMap API key
    API_KEY = "816307c0a9dd308db6ae4db5f4458eb4"
    CITY = "London"

    weather_data = fetch_weather_data(CITY, API_KEY)
    if weather_data:
        weather_df = parse_weather_data(weather_data)
        plot_weather_data(weather_df, CITY)
