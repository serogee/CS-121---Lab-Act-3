from abc import ABC, abstractmethod
from enum import Enum

class Classification(Enum):

    CAR = "car"

class Vehicle(ABC):

    def __init__(self, passenger_limit, fuel_type):
        self.passenger_limit = passenger_limit
        self.fuel_type = fuel_type

        self.__speed = 0
        self.__is_running = False

    @property
    def speed(self):
        return self.__speed
        
    @property
    def is_running(self):
        return self.__is_running

    @property
    @abstractmethod
    def classification(self):
        ...
        
    def accelerate(self):
        ...

    def decelerate(self):
        ...

    def start(self):
        ...

    def stop(self):
        ...
