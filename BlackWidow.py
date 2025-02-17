print("\n***************************************************\n")
print("Gasoline Branch - Developer: Konner Hunt\n")

import random
from time import sleep

def gasLevelGauge():
    gasLevelList = ["Full Tank", "Three Quarter Tank", "Half Tank", "Quarter Tank", "Low", "Empty"]
    return random.choice(gasLevelList)

def gasStations():
    gasStaionsList = ["Shell", "Marathon", "Speedway", "Circle K", "Wesco", "Meijer", "Sheetz", ]
    return random.choice(gasStaionsList)

def gasLevelAlert():
    milesToGasStationLow = round(random.uniform(1,25),0)
    milesToGasStationQuarterTank = round(random.uniform(25.1,50),1)
    gasLevelIndicator = gasLevelGauge()
    if gasLevelIndicator == "Empty":
        print("****WARNING - YOU ARE OUT OF GAS****\n")
        sleep(1.25)
        print("Calling AAA")
    elif gasLevelIndicator == "Low":
        print("Your gas tank is extremely low, checking GPS for the closest gas station\n")
        sleep(1.25)
        print("The closest gas station is", gasStations(), "which is",milesToGasStationLow, "miles away.")
    elif gasLevelIndicator == "Quarter Tank":
        print("Your gas tank is on a quarter tank, checking GPS for the closest gas station\n")
        sleep(1.25)
        print("The closest gas station is", gasStations(), "which is",milesToGasStationQuarterTank, "miles away.")

gasLevelAlert()