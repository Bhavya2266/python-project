import tkinter as tk
import requests

root = tk.Tk()
root.title("Weather Forecasting App")
root.geometry("400x200")


api_key = "your_api_key_here"
endpoint = "http://api.openweathermap.org/data/2.5/weather"


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
       
        temp = data["main"]["temp"]
        description = data["weather"][0]["description"]

        weather_label.config(text=f"It's {temp}°C and {description} today!")

    else:
    
        weather_label.config(text="Error: Invalid city name")


city_entry = tk.Entry(root)
city_entry.pack()

submit_button = tk.Button(root, text="Get Weather", command=get_weather_data)
submit_button.pack()

weather_label = tk.Label(root, text="")
weather_label.pack()

root.mainloop()
