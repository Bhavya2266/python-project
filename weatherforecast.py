import tkinter as tk
import requests

# Set up the window
root = tk.Tk()
root.title("Weather Forecasting App")
root.geometry("400x200")

# Define the API key and endpoint
api_key = "your_api_key_here"
endpoint = "http://api.openweathermap.org/data/2.5/weather"

# Define the function to get the weather data
def get_weather_data():
    city = city_entry.get()
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }
    response = requests.get(endpoint, params=params)

    if response.status_code == 200:
        data = response.json()
        # Extract the relevant information
        temp = data["main"]["temp"]
        description = data["weather"][0]["description"]

        # Display the weather data
        weather_label.config(text=f"It's {temp}°C and {description} today!")

    else:
        # Handle errors
        weather_label.config(text="Error: Invalid city name")

# Create the input field and button
city_entry = tk.Entry(root)
city_entry.pack()

submit_button = tk.Button(root, text="Get Weather", command=get_weather_data)
submit_button.pack()

# Create the label to display the weather data
weather_label = tk.Label(root, text="")
weather_label.pack()

root.mainloop()
