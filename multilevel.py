
class Vehicle:
    def vehicle_info(self):
        print("This is a vehicle.")



class Car(Vehicle):
    def car_info(self):
        print("Cars are used for personal transportation.")


class ElectricCar(Car):
    def electric_car_info(self):
        print("Electric cars run on batteries.")



class Bike(Vehicle):
    def bike_info(self):
        print("Bikes are two-wheeled vehicles.")



print("Multilevel Inheritance:")
tesla = ElectricCar()
tesla.vehicle_info()
tesla.car_info()
tesla.electric_car_info()

print("\nHierarchical Inheritance:")
yamaha = Bike()
yamaha.vehicle_info()
yamaha.bike_info()
