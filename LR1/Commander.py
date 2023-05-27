from Garden import Garden
from Patch import Patch
from Pests import Pests
from Plant import Plant, NAME_PLANT
from Weather import Weather
from Weed import Weed
from Timer import Timer

class Commander():
    def __init__(self):
        self.garden = Garden()
        self.weather = Weather()
        self.date = Timer()
    commands = ["add_patch", "add_plant", "add_weed", "add_pest", "patch_list", "weeding", "kill_pest",
                  "compost", "watering", "illness", "exit"]
    
    def start(self, args):
        self.date = self.garden.open(self.date)
        self.define_command(args[0], args[1:])
        self.next()
        self.garden.save(self.date)

    def define_command(self, command, args):
        try:
            if command == 'add_patch':
                self.garden.addPatch()
            elif command == 'add_plant':
                self.garden.addPlantToGarden(int(args[0]), args[1])
            elif command == 'add_weed':
                self.garden.addWeedToGarden(int(args[0]), args[1])
            elif command == 'add_pest':
                self.garden.addPestToGarden(int(args[0]), args[1])
            elif command == 'patch_list':
                try: self.garden.showPatches()
                except: pass
            elif command == 'weeding':
                self.garden.patches[int(args[0])].weeding()
                print(args[0])
            elif command == 'kill_pest':
                self.garden.patches[int(args[0])].killPests()
                print(args[0])
            elif command == 'compost':
                self.garden.patches[int(args[0])].compost()
            elif command == 'watering':
                self.garden.patches[int(args[0])].watering()
            elif command == 'illness':
                self.garden.patches[int(args[0])].illness()
            elif command == 'clear':
                self.garden.clear(self.date)
        except IndexError: print("Args error.")
            
    def next(self):
        self.garden.makeWeedDamage()
        self.garden.makePestDamage()
        self.weather.changeState()
        self.garden.weatherImpact(self.weather)
        print("Current date: ", end = " ")
        self.date.showData()
        self.date.nextDay(self.garden)
        return
