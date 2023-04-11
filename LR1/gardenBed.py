import random
import argparse
import os
from abc import ABC, abstractmethod
import re

class Plant:
    def __init__(self, name, health,water_level,growth,harvest):
        self.name = name      
        self.health = health
        self.water_level = water_level
        self.growth = growth
        self.harvest = harvest

    def grow(self):
        self.growth += 5
    def fertilizer_grow(self):
        self.growth += 10

class GardenBed:
    
    def __init__(self, plant,health,water_level,growth,harvest, weeds,diseases,fertilizer,pests,weeding, drought,watering,death):
    
        self.plant = Plant(plant,health,water_level,growth,harvest)
        self.watering = Watering(watering)
        self.drought = Drought(drought)
        self.weeds = Weeds(weeds)
        self.diseases = Diseases(diseases)
        self.fertilizer = Fertilizer(fertilizer)
        self.pests = Pests(pests)
        self.weeding1 = Weeding(weeding)
        self.death = Death(death)

    def weeding(self):
        self.weeding1 = Weeding("Yes")
        self.weeds = Weeds("No")
        self.plant.health += 2

        
    def check_weeds(self):
        if self.weeds.cheack == "Yes":
            self.plant.health -=5
    
    def check_water_level(self):
        if self.plant.water_level > 100 :
    
            self.death = Death("Yes")
   
    def check_drought(self, count_of_sunny_days):
        if count_of_sunny_days >= 2:
            self.drought = Drought("Yes")
            self.plant.water_level = self.drought.decrease_water_level(self.plant.water_level)

    def watering1(self):
        self.drought = Drought("No")
        self.watering = Watering("Yes")
        self.plant.water_level = self.watering.increase_water_level(self.plant.water_level)
    
    def check_fertilizer(self):
        if self.fertilizer.cheack == "Yes":
            self.plant.fertilizer_grow()
            self.plant.harvest +=10

    def harvesting(self): 
        if self.plant.harvest > 100:
            self.plant.harvest = 0

    def check_pests(self):
        if self.pests.cheack == "Yes":
            self.plant.health -= 10

    def delete_pests(self):
        self.pests = Pests("No")
        self.plant.health +=2

    def check_diseases(self):
        if self.diseases.cheack == "Yes":
            self.plant.health -= 10

    def delete_diseases(self):
        self.diseases = Diseases("No")
        self.plant.health +=2

    def check_health(self):
        if self.plant.health <= 0:
            self.death = Death("Yes")
        if self.plant.growth >= 100:
            self.growth = 100

class Garden(GardenBed, Plant):

    def __init__(self):
        self.weather : Weather = None
        self.garden = []
        self.count_of_sunny_days = 0
        self.count_of_rainy_days = 0

    def generate_weather(self):
        sun, rain = Sun(), Rain()
        conditions = [sun, rain] 
        self.weather = random.choice(conditions) 
        return self.weather
    
    def rainy_day(self, i):
        if self.weather.get_type() == "rainy":
            self.garden[i].watering = Watering("No")
            self.garden[i].drought = Drought("No")
            self.garden[i].plant.water_level +=5
        if self.garden[i].plant.water_level > 100:
            self.garden[i].plant.health -=5
        if self.weather.get_type() == "sunny":
            self.garden[i].plant.water_level -=5
            if self.garden[i].plant.health < 100:
                self.garden[i].plant.health +=5

    def count_sunny_or_rainy_days(self):
        if self.weather.get_type() == "sunny":
            self.count_of_sunny_days +=1
            self.count_of_rainy_days = 0
              

        if self.weather.get_type() == "rainy":
            self.count_of_sunny_days = 0
            self.count_of_rainy_days += 1 
       

    def read_garden_from_file(self, file1):
        file = open(file1, 'r')
        garden = file.readlines()
        for garden_bed in garden:
            garden_bed =garden_bed.split()
            gardenBed = GardenBed(garden_bed[0], int(garden_bed[1]), int(garden_bed[2]), int(garden_bed[3]), int(garden_bed[4]), garden_bed[5], garden_bed[6], garden_bed[7] ,garden_bed[8], garden_bed[9], garden_bed[10], garden_bed[11], garden_bed[12])
           
            self.garden.append(gardenBed)
        file.close()
    def state_change(self, i, new_weeds, new_diseases, new_fertilizer, new_pests):
        self.garden[i].weeds = Weeds(new_weeds)
        self.garden[i].diseases = Diseases(new_diseases)
        self.garden[i].fertilizer = Fertilizer(new_fertilizer)
        self.garden[i].pests = Pests(new_pests)

    def simulation(self, file2):
        i = 0
        str_index = 0
        plants_that_should_be_delete = []

        file20 = open(file2, 'r')
        states = file20.readlines()
       
        for state in states:
            state =state.split()
            
            if state == ['day']:
                try:
                    input("Press Enter to go to the next step")
                except TypeError:
                    print("The end")
                    break
                
                self.weather = self.generate_weather()
                print(self.weather.get_type())
                self.count_sunny_or_rainy_days()              
                
                i = 0
            if state != ['day']: 
                self.state_change(i, state[1], state[2], state[3] ,state[4])

                self.rainy_day(i)
                self.garden[i].check_water_level()
                self.garden[i].check_diseases()
                self.garden[i].check_weeds()
                self.garden[i].check_pests()
                self.garden[i].check_health()
                
                if self.garden[i].death.cheack == "Yes":
       
                    if self.garden[i].plant.name in plants_that_should_be_delete:
                        i+=1
                        try:
         
                            if states[str_index+1] == 'day\n':
                                self.display_plants(plants_that_should_be_delete)
                        except IndexError:
                                self.display_plants(plants_that_should_be_delete)
                                self.safe_state()
                                break 
            
                        str_index+=1
                    
                    else:
                        plants_that_should_be_delete.append(self.garden[i].plant.name)
                        i+=1
                        try:
         
                            if states[str_index+1] == 'day\n':
                                self.display_plants(plants_that_should_be_delete)
                        except IndexError:
                                self.display_plants(plants_that_should_be_delete)
                                self.safe_state()
                                break 
            
                        str_index +=1
                    continue
                        
               
                if self.garden[i].weeds.cheack == "Yes":
                    self.garden[i].weeding()

               
                if self.garden[i].diseases.cheack == "Yes":
                    self.garden[i].delete_diseases()

                self.garden[i].check_fertilizer()

                
                if self.garden[i].pests.cheack == "Yes":
                    self.garden[i].delete_pests()
               
                self.garden[i].check_drought(self.count_of_sunny_days)
                if self.garden[i].drought.cheack == "Yes":
                    self.garden[i].watering1()
              
                
                if self.garden[i].plant.growth >= 100:
                    self.garden[i].plant.growth = 100
                else:
                    self.garden[i].plant.grow()

                
                self.garden[i].harvesting()
                
                i+=1
            
            try:
              
                if states[str_index+1] == 'day\n':
                    self.display_plants(plants_that_should_be_delete)
            except IndexError:
                    self.display_plants(plants_that_should_be_delete)
                    self.safe_state()
                    break 
            
            str_index +=1
        file20.close()  
        for i in range(0, len(plants_that_should_be_delete)):
            self.delete_gardenBed(plants_that_should_be_delete[i])
                   
        

    def display_plants(self, plants_that_should_be_delete):
     
        if len(self.garden) == 0 or \
            len(self.garden) == len(plants_that_should_be_delete):
            print("There are no plants in your garden.")
        else:
            print("Here are the plants in your garden:")
            print("{:<5} {:<20} {:<10} {:<15} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format("No.", "Name", "Health", "Water Level", "Growth", "Harvest","Weeds","Diseases", "Fertilizer", "Pests", "Weeding","Drought", "Watering", "Death"))
            for i in range(len(self.garden)):
               
                    if self.garden[i].plant.harvest == 100:
                        harvest_status = "Ready"
                    else:
                        harvest_status = "-"

                    if self.garden[i].death.cheack == "Yes":
                        continue
                   
                    print("{:<5} {:<20} {:<10} {:<15} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format(i+1, self.garden[i].plant.name, self.garden[i].plant.health, self.garden[i].plant.water_level, self.garden[i].plant.growth, harvest_status, self.garden[i].weeds.cheack, self.garden[i].diseases.cheack, self.garden[i].fertilizer.cheack, self.garden[i].pests.cheack, self.garden[i].weeding1.cheack, self.garden[i].drought.cheack, self.garden[i].watering.cheack, self.garden[i].death.cheack))
                    

    def safe_state(self):
        file = open("garden.txt", "w")
     
        for i in range(0,len(self.garden)):
            
            file.write(self.garden[i].plant.name + ' ' + str(self.garden[i].plant.health) + ' ' + str(self.garden[i].plant.water_level) + ' ' +str(self.garden[i].plant.growth) + ' ' +str(self.garden[i].plant.harvest) + ' ' +str(self.garden[i].weeds.cheack) + ' ' +str(self.garden[i].diseases.cheack) + ' ' +str(self.garden[i].fertilizer.cheack) + ' ' +str(self.garden[i].pests.cheack) + ' ' +str(self.garden[i].weeding1.cheack) + ' ' +str(self.garden[i].drought.cheack) + ' ' +str(self.garden[i].watering.cheack)+ ' ' + str(self.garden[i].death.cheack)+"\n")
        file.close()

    def delete_gardenBed(self, delete_plant):
        
        for i in range(0, len(self.garden)):
            if self.garden[i].plant.name == delete_plant:
                plant1 = self.garden[i].plant.name
                self.garden.remove(self.garden[i])
                break
        if plant1 == delete_plant:
            f = open("garden.txt", "r+")
            plants_in_garden = f.readlines()
            f.seek(0)
            for plant in plants_in_garden:
                if not re.search(delete_plant,plant):
                    f.write(plant)
            f.truncate()
            f.close()

         
            f = open("states.txt", "r+")
            states_plant_in_garden = f.readlines()
            f.seek(0)
            for state_plant in states_plant_in_garden:
                if not re.search(delete_plant,state_plant):
                    f.write(state_plant)
            f.truncate()
            f.close()
        
def add_gardenBed(plant):
    if plant == "skip":
        return False
    file = open("garden.txt", "a")
    gardenBed = GardenBed(plant,100,100,0,0, "No","No","No","No","No","No","No","No")
    file.write(gardenBed.plant.name + ' ' + str(gardenBed.plant.health) + ' ' + str(gardenBed.plant.water_level) + ' ' +str(gardenBed.plant.growth) + ' ' +str(gardenBed.plant.harvest) + ' ' +str(gardenBed.weeds.cheack) + ' ' +str(gardenBed.diseases.cheack) + ' ' +str(gardenBed.fertilizer.cheack) + ' ' +str(gardenBed.pests.cheack) + ' ' +str(gardenBed.weeding1.cheack) + ' ' +str(gardenBed.drought.cheack) + ' ' +str(gardenBed.watering.cheack)+ ' '+ str(gardenBed.death.cheack)+"\n")
    file.close()
    return True

def add_states_for_new_plant(plant):
    number_of_plants = 0
    new_state = []
    file3 = open("garden.txt", "r")
    plants = file3.readlines()
    for plant1 in plants:
        number_of_plants +=1
    file3.close
    file1 = open("states.txt", "r+")
    states1 = file1.readlines()
    file1.seek(0)
    file_new_states = open("state_for_new_plant.txt", "r")
    new_state = file_new_states.readline()
    new_state = new_state.split()
    file_new_states.seek(0)
    i=0
    day = 1
  
    for state in states1:
        if state == 'day\n':
            # print("Enter state for ", day, " day ")
            weeds = new_state[0]#input("Enter Yes/No for weeds ")
            diseases = new_state[1]#input("Enter Yes/No for diseases ")
            fertilizer = new_state[2]#input("Enter Yes/No for fertilizer ")
            pests = new_state[3]#input("Enter Yes/No for pests ")
            str1 = plant + ' ' + weeds + ' ' + diseases + ' ' + fertilizer + ' ' + pests + "\n"
            states1.insert(i+number_of_plants,str1 )
            day+=1

        file1.write(state)
        i+=1
   
       
    file1.close()

    
def run(start, delete_plant):
    if start == "run":
        garden =Garden()

        garden.read_garden_from_file("garden.txt")
        if delete_plant != "skip delete":
            garden.delete_gardenBed(delete_plant)
        garden.simulation("states.txt")
         




class Weather(ABC):
 

    @abstractmethod
    def get_type(self):
        return self.type

class Sun(Weather):
    def __init__(self):
        self.type = "sunny"

    def get_type(self):
        return self.type

class Rain(Weather):
    
    def __init__(self):
        self.type = "rainy"

    def get_type(self):
        return self.type

class Watering:
    def __init__(self, cheack):
        self.cheack = cheack

    def increase_water_level(self, water_level):
        water_level +=5
        return water_level

class Drought:
    def __init__(self, cheack):
        self.cheack = cheack

    def decrease_water_level(self, water_level):
        water_level-=10
        return water_level
        

class Weeds:
    def __init__(self, cheack):
        self.cheack = cheack


class Diseases:
    def __init__(self, cheack):
        self.cheack = cheack

class Pests:
    def __init__(self, cheack):
        self.cheack = cheack

class Fertilizer:
    def __init__(self, cheack):
        self.cheack = cheack

class Weeding:
    def __init__(self, cheack):
        self.cheack = cheack

class Death:
    def __init__(self, cheack):
        self.cheack = cheack

def main(): 
    parser = argparse.ArgumentParser(description="Simulate a garden plot with weather conditions and plant life cycles.")
    parser.add_argument("run", type=str, help="Run the code")
    parser.add_argument("--add_plant",type = str, default="skip", help="Add the garden bed")
    parser.add_argument("--delete_plant",type = str, default="skip delete", help="Delete the garden bed")

    args = parser.parse_args()

    add = add_gardenBed(args.add_plant)
    if add == True:
        
       add_states_for_new_plant(args.add_plant)

    run(args.run,args.delete_plant)

if __name__ == "__main__":
    main()
