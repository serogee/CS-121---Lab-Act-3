from abc import ABC, abstractmethod

class Vehicle(ABC):

    def __init__(self, speed, passenger_limit, fuel_type):
        self.speed = speed
        self.passenger_limit = passenger_limit
        self.fuel_type = fuel_type

    @property
    @abstractmethod
    def classification(self):
        pass

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def drive(self):
        pass
