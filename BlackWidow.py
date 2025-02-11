# Import necessary libraries
import sys  # To interact with system-specific parameters and functions
import time  # To handle time-related tasks, like sleep delays

# ANSI escape codes for colors
RESET = "\033[0m"  # Reset to default color
RED = "\033[31m"  # Red text
GREEN = "\033[32m"  # Green text
YELLOW = "\033[33m"  # Yellow text
CYAN = "\033[36m"  # Cyan text
WHITE = "\033[97m"  # White text

# Print a welcome message with the developer's name in green
print(CYAN + "\nWelcome Branch - Developer: Konner Hunt" + RESET)

# Print the InfoTechCenter system version in cyan
print(CYAN + "\nWelcome to InfoTechCenter v1.0\n" + RESET)

# Initialize variables
x = 0  # Counter for the booting process (keeps track of boot steps)
ellipsis = 0  # Counter for the number of dots in the booting message (controls loading effect)

# Loop to simulate the system booting process
while x != 20:
    x += 1  # Increment the counter to simulate boot steps
    # Construct the booting message with dynamic dots for a loading effect
    message = ("Infotech Center System Booting" + "." * ellipsis)
    ellipsis += 1  # Increase the number of dots in the message to simulate loading progress
    sys.stdout.write("\r" + RED + message + RESET)  # Print the message in yellow with carriage return to overwrite previous output
    time.sleep(.5)  # Pause for 0.5 seconds between each step to simulate progress

    # Reset the ellipsis counter after reaching 4 dots
    if ellipsis == 4:
        ellipsis = 0  # Reset the ellipsis counter to restart the cycle of dots

    # When the loop reaches 20 iterations (booting completed), print the system's status in green
    if x == 20:
        print("\n\n" + GREEN + "Operating System Booted Up - Retina Scanned - Access Granted\n" + RESET)

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
