print("\n***************************************\n")
print("Weather Branch - Developer: Konner Hunt")

# Import necessary libraries
import random
from time import sleep

# Function to determine the weather condition
def weather():
    weatherForecastList = ["snowing", "blizzard", "icy", "rainy", "windy", "sunny"]
    return random.choice(weatherForecastList)  # Randomly select a weather condition

# Weather response mapping: weather condition -> (delay, speed)
weather_response = {
    "snowing": (30, 55),
    "blizzard": (60, 45),
    "icy": (90, 35),
    "rainy": (10, 65),
    "windy": (5, 70),
    "sunny": (0, 0)  # Assume 0 delay and no speed restriction for sunny
}

# Get the current weather condition
weatherAlert = weather()

# Function to determine the vehicle response based on the weather condition
def vehicleResponseSystem():
    # Get the delay and speed from the dictionary
    delay, speed = weather_response.get(weatherAlert, (0, 0))

    if weatherAlert == "sunny":
        print(f"\nThe National Weather Service reports it is a beautiful {weatherAlert} day today.")
        print("\nVRS has been disengaged, drive safe!")
    else:
        print(f"\nThe National Weather Service has updated your alarm by {delay} minutes because it is {weatherAlert} outside.")
        sleep(1)
        print(f"\nVRS has been engaged only allowing us to drive {speed}MPH.")

# Execute the vehicle response system
vehicleResponseSystem()
