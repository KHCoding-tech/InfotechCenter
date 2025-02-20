# Import necessary libraries
import sys  # To interact with system-specific parameters and functions
import time  # To handle time-related tasks, like sleep delays
import random
from time import sleep

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
        print("\n\n" + GREEN + "Operating System Booted Up - Retina Scanned - Access Granted" + RESET)

# Function to randomly determine the gas level
def gasLevelGauge():
    return random.choice(["Full Tank", "Three Quarter Tank", "Half Tank", "Quarter Tank", "Low", "Empty"])


# Function to randomly select a gas station
def gasStations():
    return random.choice(["Shell", "Marathon", "Speedway", "Circle K", "Wesco", "Meijer", "Sheetz"])


# Function to check gas level and provide alerts accordingly
def gasLevelAlert():
    gasLevelIndicator = gasLevelGauge()  # Get a random gas level
    station = gasStations()  # Get a random gas station

    # Dictionary mapping gas levels to corresponding messages
    gas_messages = {
        "Empty": [
            "****WARNING - YOU ARE OUT OF GAS****\n",
            "Calling AAA..."
        ],
        "Low": [
            "Your gas tank is extremely LOW.\n",
            "Checking GPS for the closest gas station...\n",
            f"The closest gas station is {station}, which is {round(random.uniform(1, 25), 0)} miles away."
        ],
        "Quarter Tank": [
            "Your gas tank is on a QUARTER TANK.\n",
            "Checking GPS for the closest gas station...\n",
            f"The closest gas station is {station}, which is {round(random.uniform(25.1, 50), 1)} miles away."
        ],
        "Half Tank": [
            "Your gas tank is on HALF A TANK.\n",
            "That's enough to get to your destination."
        ],
        "Three Quarter Tank": [
            "Your gas tank is on THREE QUARTERS OF A TANK."
        ],
        "Full Tank": [
            "Your gas tank is FULL."
        ]
    }

    # Print the header with delays
    print("\n***************************************************\n")

    print("Gasoline Branch - Developer: Konner Hunt\n")
    sleep(1)

    # Print the appropriate messages for the detected gas level, adding a delay between lines
    for message in gas_messages[gasLevelIndicator]:
        print(message)
        sleep(1.25)


# Run the gas level alert function
gasLevelAlert()

print("\n***************************************\n")
print("Weather Branch - Developer: Konner Hunt")

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

