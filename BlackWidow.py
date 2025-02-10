print("\n***************************************\n")

print("Weather Branch - Developer: Konner Hunt\n")

#Import Libraries HERE
import random
from time import sleep

# Weather Function to determine the weather
def weather():
    weatherForecastList = ["snowing", "blizzard", "icy", "rainy", "windy", "sunny"]
    weatherCondition = random.choice(weatherForecastList)
    return weatherCondition

weatherAlert = weather()

def vehicleResponseSystem():
    if weatherAlert == "snowing":
        print("\nThe National Weather Service has updated your alarm by 30 minutes because"
              " it is", weatherAlert, "outside.\n")
    elif weatherAlert == "blizzard":
        print("\n The National Weather Service has updated your alarm by 60 minutes because"
              " it is a", weatherAlert, "outside.\n")
    elif weatherAlert == "icy":
        print("\n The National Weather Service has updated your alarm by 90 minutes because"
              " it is", weatherAlert, "outside.\n")
    elif weatherAlert == "rainy":
        print("\n The National Weather Service has updated your alarm by 10 minutes because"
              " it is", weatherAlert, "outside.\n")
    elif weatherAlert == "windy":
        print("\n The National Weather Service has updated your alarm by 5 minutes because"
              " it is", weatherAlert, "outside.\n")
    else:
        print("\n The National Weather Service reports it is a beautiful", weatherAlert, "day today.\n")
        
vehicleResponseSystem()