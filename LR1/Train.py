import Randomazer
import time

class Train:
    MAX_PASS_BY_CAR = 50
    MAX_MASS_BY_CAR = 68
    SPEED_LOST_BY_MASS = 0.005
    SPEED_LOST_BY_PASSENGERS = 0.001
    SPEED_LOST_BY_CAR = 0.5

    def __init__(self, default_train_speed, pass_cars, freight_cars):
        self.default_train_speed = default_train_speed
        self.pass_cars = pass_cars
        self.freight_cars = freight_cars
        self.actual_pass = 0
        self.actual_mass = 0
        self.actual_train_speed = default_train_speed

    def processPassengers(self, station):
        randomazer = Randomazer.Randomazer()
        passengersLeave = randomazer.generateRandomValue(0, self.actual_pass)
        print(f"Train lose {passengersLeave} passengers")
        self.actual_pass -= passengersLeave
        passengersGet = randomazer.generateRandomValue(0, (self.MAX_PASS_BY_CAR * self.pass_cars) - self.actual_pass)
        print(f"Train get {passengersGet} passengers")
        self.actual_pass += passengersGet
        print(f"- In train now {self.actual_pass} passengers")

    def processFreight(self, station):
        randomazer = Randomazer.Randomazer()
        massLeave = randomazer.generateRandomValue(0, self.actual_mass)
        print(f"Train lose {massLeave} tons")
        self.actual_mass -= massLeave
        massGet = randomazer.generateRandomValue(0, (self.MAX_MASS_BY_CAR * self.freight_cars) - self.actual_mass)
        print(f"Train get {massGet} tons")
        self.actual_mass += massGet
        print(f"- In train now {self.actual_mass} tons")

    def calculateSpeed(self, station):
        self.actual_train_speed -= (self.actual_mass * self.SPEED_LOST_BY_MASS) + (
                    self.actual_pass * self.SPEED_LOST_BY_PASSENGERS)
        print(f"Now train is moving {self.actual_train_speed} km/h")
        print(f"Distance to the next station {station.getDistanceToNextStation()} kilometers")
        times = station.getDistanceToNextStation() / self.actual_train_speed
        print(f"Train will arrive to the next station after {times} hours")
        time.sleep(times * 10)

    def processStation(self, station, isLast):
        print("\t\tTrain arrive to " + station.getStationName())

        if not isLast:
            stationType1 = station.getStationType()
            if stationType1 == 1:
                self.processPassengers(station)
                self.processFreight(station)
                self.calculateSpeed(station)
            elif stationType1 == 2:
                self.processPassengers(station)
                self.calculateSpeed(station)
            elif stationType1 == 3:
                self.processFreight(station)

                self.calculateSpeed(station)
        else:
            print("Train lose " + str(self.actual_pass) + " passengers")
            self.actual_pass -= self.actual_pass
            print("Train get 0 passengers")
            print("- In train now " + str(self.actual_pass) + " passengers")

            print("Train lose " + str(self.actual_mass) + " tons")
            self.actual_mass -= self.actual_mass
            print("Train get 0 tons")
            print("- In train now " + str(self.actual_mass) + " tons")
            print("\t\t\tTrain is STOPPED!!!")

        print("===================================")

    class Train:
        def __init__(self):
            pass_cars = int(input("Passenger cars - "))
            freight_cars = int(input("Freight cars - "))
            default_train_speed = float(input("Default speed - "))
            self.pass_cars = pass_cars
            self.freight_cars = freight_cars
            self.default_train_speed = default_train_speed
            self.actual_train_speed = default_train_speed

