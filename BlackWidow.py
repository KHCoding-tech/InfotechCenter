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
              " it is", weatherAlert, "outside")
        
vehicleResponseSystem()