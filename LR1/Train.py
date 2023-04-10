class Locomotive:
    def __init__(self,speed):
        self.current_speed=speed
    def set_speed(self,speed):
        self.current_speed = speed

class TrainCar:
    def __init__(self):
        self.current_occupancy=0
        self.max_occupancy=100
        self.cargo_type="Idle"
    def get_current_occupancy(self):
        return self.current_occupancy
    def load(self,cargo_type,value):
        if value <= self.max_occupancy:
            self.current_occupancy=value
            self.set_cargo_type(cargo_type)
        else:
            print("Exception load_value is more than max_traincar_occupancy")
    def unload(self,type):
        if(self.cargo_type==type):
            tmp = self.current_occupancy
            self.current_occupancy=0
            self.cargo_type="Idle"
            return tmp
    def get_cargo_type(self):
        return self.cargo_type
    def set_cargo_type(self,type):
        self.cargo_type=type
    def __str__(self):
        result = ("{:>18}  {:>17}  {:>17}".format(
            self.current_occupancy,
            self.max_occupancy,
            self.cargo_type,
        ))
        return result
        


class Train:
    def __init__(self,train_number,locomotive_speed,traincar_value):
        self.train_number=train_number
        self.locomotive=Locomotive(locomotive_speed)
        self.trainCars =[TrainCar() for _ in range(traincar_value)]
        self.current_task="Idle"
        self.current_task_type="Idle"
        self.current_position=1
        self.train_speed=self.locomotive.current_speed
    def calculate_current_speed(self):
         self.train_speed-=len(self.trainCars)*2
    def trainCar_value(self):
        return len(self.trainCars)
    def load_train(self,load_value):
        for item in self.trainCars:
            item.load(load_value)
    def unload_train(self):
        unload_value=0
        for item in self.trainCars:
            unload_value+=item.unload()
        return unload_value
    def set_current_task(self,task):
        self.current_task = task
    def get_current_task(self):
        return self.current_task
    def set_current_task_type(self,task_type):
        self.current_task_type=task_type
    def get_current_task_type(self):
        return self.current_task_type
    def get_current_load_status(self):
        if(self.trainCars[0].get_current_occupancy()!=0):
            return True
        else: 
            return False
    def get_trainCars(self):
        return self.trainCars
    def get_train_number(self):
        return self.train_number
    def get_train_speed(self):
        return self.train_speed
    def get_current_position(self):
        return self.current_position
    def set_current_position(self,position):
        self.current_position=position
    def __str__(self):
        result=""
        result+=f"Train number: {self.train_number} \n"
        result+=f"Traincars({len(self.trainCars)}):\n"
        result+=("{:>18}  {:>18}  {:>18}".format(
            "Current_occupancy:","Max_occupancy:","Cargo_type:\n"))
        for _ in self.trainCars:
            result+=str(_)+"\n"       
        result+=f"TrainSpeed: {self.train_speed} \n"
        return result
