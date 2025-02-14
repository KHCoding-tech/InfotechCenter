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


print(gasLevelGauge())
print(gasStations())