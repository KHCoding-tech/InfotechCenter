print("\n***************************************\n")

print("Weather Branch - Developer: Konner Hunt")

# Import necessary libraries
import random
from time import sleep

# Function to determine the weather condition
def weather():
    weatherForecastList = ["snowing", "blizzard", "icy", "rainy", "windy", "sunny"]
    weatherCondition = random.choice(weatherForecastList)  # Randomly select a weather condition
    return weatherCondition

# Get the current weather condition
weatherAlert = weather()

# Function to determine the vehicle response based on the weather condition
def vehicleResponseSystem():
    if weatherAlert == "snowing":
        print("\nThe National Weather Service has updated your alarm by 30 minutes because"
              " it is", weatherAlert, "outside.")
        sleep(1)
        print("\nVRS has been engaged only allowing us to drive 55MPH.")
    elif weatherAlert == "blizzard":
        print("\nThe National Weather Service has updated your alarm by 60 minutes because"
              " it is a", weatherAlert, "outside.")
        sleep(1)
        print("\nVRS has been engaged only allowing us to drive 45MPH.")
    elif weatherAlert == "icy":
        print("\nThe National Weather Service has updated your alarm by 90 minutes because"
              " it is", weatherAlert, "outside.")
        sleep(1)
        print("\nVRS has been engaged only allowing us to drive 35MPH.")
    elif weatherAlert == "rainy":
        print("\nThe National Weather Service has updated your alarm by 10 minutes because"
              " it is", weatherAlert, "outside.")
        sleep(1)
        print("\nVRS has been engaged only allowing us to drive 65MPH.")
    elif weatherAlert == "windy":
        print("\nThe National Weather Service has updated your alarm by 5 minutes because"
              " it is", weatherAlert, "outside.")
        sleep(1)
        print("\nVRS has been engaged only allowing us to drive 70MPH.")
    else:
        print("\nThe National Weather Service reports it is a beautiful", weatherAlert, "day today.")
        sleep(1)
        print("\nVRS has been disengaged, drive safe!")

# Execute the vehicle response system
vehicleResponseSystem()
