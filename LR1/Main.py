import json
import sys
from Garden import Garden
from Patch import Patch
from Pests import Pests
from Plant import Plant, NAME_PLANT
from Weather import Weather
from Weed import Weed
from Timer import Timer
from Commander import Commander


def main():
    commander = Commander()
    if len(sys.argv) > 1:
        commander.start(sys.argv[1:])

if __name__ == "__main__":
    main()



# while(True):
    # print("Write the command:")
    # command = input()
    # if(command == "add_patch"):
    #     garden.addPatch()
    # elif(command == "add_plant"):
    #     number = int(input()) - 1
    #     garden.addPlantToGarden(number)
    # elif(command == "add_weed"):
    #     print("Choose the number of patch:")
    #     number = int(input()) - 1
    #     if(number < 0):
    #         number = 0
    #     garden.addWeedToGarden(number, 0, True)
    # elif(command == "add_pest"):
    #     print("Choose the number of patch:")
    #     number = int(input()) - 1
    #     if(number < 0):
    #         number = 0
    #     garden.addPestToGarden(number, 0, True)
    # elif(command == "patch_list"):
    #     garden.showPatches()
    # elif(command == "weeding"):
    #     print("Choose the number of patch:")
    #     number = int(input()) - 1
    #     if(number < 0):
    #         number = 0
    #     garden.patches[number].weeding()
    #     print(str(number + 1))
    # elif(command == "kill_pest"):
    #     print("Choose the number of patch:")
    #     number = int(input()) - 1
    #     if(number < 0):
    #         number = 0
    #     garden.patches[number].killPests()
    #     print(str(number + 1))
    # elif(command == "compost"):
    #     print("Choose the number of patch:")
    #     number = int(input()) - 1
    #     if(number < 0):
    #         number = 0
    #     garden.patches[number].compost()
    # elif(command == "watering"):
    #     print("Choose the number of patch:")
    #     number = int(input()) - 1
    #     if(number < 0):
    #         number = 0
    #     garden.patches[number].watering()
    # elif(command == "illness"):
    #     print("Choose the number of patch:")
    #     number = int(input()) - 1
    #     if(number < 0):
    #         number = 0
    #     garden.patches[number].illness()
    # elif(command == "exit"):
    #     break
    # else:
    #     print("This command is missing")
    # garden.makeWeedDamage()
    # garden.makePestDamage()
    # weather.changeState()
    # garden.weatherImpact(weather)
    # print("Current date: ", end = " ")
    # data.showData()
    # data.nextDay(garden)