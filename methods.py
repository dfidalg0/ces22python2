# Exercício 8

from abc import ABC, abstractmethod

class Register (ABC):
    # Static methods
    def count():
        return Register.__number

    # Static params
    __number = 0

    # Class methods
    def __init__ (self, name, age):
        self.__name = name
        self.__age = age
        Register.__number += 1

    def __del__ (self):
        Register.__number -= 1

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    @abstractmethod
    def get_paycheck (self):
        pass

class Dev (Register):
    junior = 0
    middle = 1
    senior = 2

    __paycheck = [5000, 10000, 15000]

    def __init__ (self, name, age, experience):
        super().__init__(name,age)
        self.__expr = experience

    def get_paycheck(self):
        return Dev.__paycheck[self.__expr]
