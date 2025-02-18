import random
from time import sleep


def gasLevelGauge():
    return random.choice(["Full Tank", "Three Quarter Tank", "Half Tank", "Quarter Tank", "Low", "Empty"])


def gasStations():
    return random.choice(["Shell", "Marathon", "Speedway", "Circle K", "Wesco", "Meijer", "Sheetz"])


def gasLevelAlert():
    gasLevelIndicator = gasLevelGauge()
    station = gasStations()  # Call once when needed

    gas_messages = {
        "Empty": ["****WARNING - YOU ARE OUT OF GAS****\n", "Calling AAA..."],
        "Low": ["Your gas tank is extremely LOW.\n",
                "Checking GPS for the closest gas station...\n",
                f"The closest gas station is {station}, which is {round(random.uniform(1, 25), 0)} miles away."],
        "Quarter Tank": ["Your gas tank is on a QUARTER TANK.\n",
                         "Checking GPS for the closest gas station...\n",
                         f"The closest gas station is {station}, which is {round(random.uniform(25.1, 50), 1)} miles away."],
        "Half Tank": ["Your gas tank is on HALF A TANK.\n", "That's enough to get to your destination."],
        "Three Quarter Tank": ["Your gas tank is on THREE QUARTERS OF A TANK."],
        "Full Tank": ["Your gas tank is FULL."]
    }

    print("\n***************************************************\n")
    sleep(1)
    print("Gasoline Branch - Developer: Konner Hunt\n")
    sleep(1)

    for message in gas_messages[gasLevelIndicator]:
        print(message)
        sleep(1.25)


gasLevelAlert()
