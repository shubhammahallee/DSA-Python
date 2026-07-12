from abc import ABC, abstractmethod

# Abstract Class
class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass
        
# Child Class 1
class Car(Vehicle):

    def start(self):
        print("Car Started")

    def stop(self):
        print("Car Stopped")


# Child Class 2
class Bike(Vehicle):

    def start(self):
        print("Bike Started")

    def stop(self):
        print("Bike Stopped")


# Driver Code
car = Car()
car.start()
car.stop()





bike = Bike()
bike.start()
bike.stop()
