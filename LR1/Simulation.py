import Db_Utility
import Railway_station
import random
import os
class Simulation:
    cargo_types = ['Coal', 'Oil', 'Natural gas', 'Grain', 'Fertilizer', 'Timber', 'Iron ore', 'Steel',
                'Cement', 'Salt', 'Copper', 'Aluminum', 'Zinc', 'Lead', 'Gold', 'Silver', 'Platinum',
                'Palladium', 'Diamonds', 'Pharmaceuticals', 'Chemicals', 'Plastics', 'Rubber', 'Textiles',
                'Leather', 'Food products', 'Beverages', 'Tobacco', 'Coffee', 'Tea', 'Cocoa', 'Sugar', 
                'Fish', 'Meat','Poultry', 'Dairy products', 'Fresh fruits', 'Fresh vegetables', 'Frozen foods',
                'Canned goods','Electronic devices', 'Automobiles', 'Machinery', 'Heavy equipment', 'Aircraft',
                'Marine vessels','Weapons', 'Military vehicles', 'Artworks', 'Antiques']

    def __init__(self,movement_cycles_value=None):
        self.graph=Db_Utility.load_graph_data()
        self.create_railway_stations()
        self.create_trains()
        self.create_tasks()
        for task in self.tasks:
            print(f"{task}")
        print('\n')
        self.movement_simulation(movement_cycles_value)


    def create_railway_stations(self):
        self.railway_stations=[]
        for vertex in self.graph.get_vertecies():
            self.railway_stations.append(Railway_station.Railway_station(vertex))
        chunk_size = len(self.cargo_types) // self.graph.get_verticies_value()  
        remainder = len(self.cargo_types) % self.graph.get_verticies_value()
        chunks = []
        start = 0
        for i in range(self.graph.get_verticies_value()):
            if i < remainder:
                end = start + chunk_size + 1
            else:
                end = start + chunk_size
            chunks.append(self.cargo_types[start:end])
            start = end
            index=0
        for station in self.railway_stations:
            for chunk in chunks[index]:
                station.load_to_stock(chunk,1000)           
            index+=1
        
    def create_trains(self):
        self.trains=[]
        self.trains=Db_Utility.load_train_data()

    def create_tasks(self):
        self.tasks=[]
        for train in self.trains:
            if train.get_current_load_status():
                range_start = 1
                range_end = self.graph.get_verticies_value()
                exclude_vertex = train.get_current_position()
                randomed_vertex = random.choice([num for num in range(range_start, range_end+1) if num != exclude_vertex])
                self.tasks.append({"train_number":train.get_train_number(),"task":randomed_vertex,"status":"uncompleted."})
                train.set_current_task({"id":randomed_vertex})
                train.set_current_task_type("unload")
            else:
                valid_list=[x for x in self.cargo_types if x not in self.railway_stations[train.get_current_position()-1].get_all_stock_cargo()]
                randomed_cargo=random.choice(valid_list)
                self.tasks.append({"train_number":train.get_train_number(),"task":randomed_cargo,"status":"uncompleted."})
                train.set_current_task(randomed_cargo)
                train.set_current_task_type("load")
                self.cargo_types.remove(randomed_cargo)
        self.create_paths()
    
    def create_paths(self):
        self.paths=[]
        for train in self.trains:
            for station in self.railway_stations:
                if isinstance(train.get_current_task(),dict):
                    if station.get_rs_number()==train.get_current_task()["id"]:
                        self.paths.append(self.graph.find_all_paths(train.get_current_position(),station.get_rs_number())[0])
                else:
                    if station.get_stock_info(train.get_current_task()):
                        self.paths.append(self.graph.find_all_paths(train.get_current_position(),station.get_rs_number())[0])
        self.paths_distances=[]
        for path in self.paths:
            path_distance=[]
            for index in range(len(path)-1):
                path_distance.append(self.graph.get_weight(path[index],path[index+1]))
            self.paths_distances.append(path_distance)
            path_distance=[]
        for item in self.paths:
            item.pop(0)        


    def movement_simulation(self,movement_cycles_value=None,auto_mode=True):
        cycle_completed_tasks_value=0
        while True:
            if cycle_completed_tasks_value!=len(self.paths):
                for index in range(len(self.paths_distances)):
                    if self.paths_distances[index]:
                        if self.paths_distances[index][0] <=0:
                            station_number=self.paths[index].pop(0)
                            station_index=station_number-1
                            print(f"Simulation:\n\t Train #: {self.trains[index].get_train_number()} arrived at: {station_number}")
                            self.paths_distances[index].pop(0)
                            if not self.paths[index]:
                                print(f"Simulation: \n\t{self.railway_stations[station_index]}")
                                if self.trains[index].get_current_task_type() == "unload":
                                    self.railway_stations[station_index].unload_train(self.trains[index])
                                else:    
                                    self.railway_stations[station_index].load_train(self.trains[index],self.trains[index].get_current_task(),1000)
                                print(f"Simulation: \n\t{self.trains[index]}")
                                print(f"Simulation: \n\t{self.railway_stations[station_index]}")
                                self.trains[index].set_current_position(self.railway_stations[station_index].get_rs_number())
                                self.tasks[index]["status"]="completed."
                                cycle_completed_tasks_value+=1
                            else:
                                continue
                        else:
                            self.paths_distances[index][0]-=self.trains[index].get_train_speed()
                    else:
                        continue
            else:
                movement_cycles_value-=1
                if movement_cycles_value<=0:
                    break
                else:
                    cycle_completed_tasks_value=0
                    input("Press Enter to continue...")
                    os.system('clear')
                    self.create_tasks()
                    for task in self.tasks:
                        print(f"{task}")
                    print('\n')