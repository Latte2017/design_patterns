#A high level should never depend on low level class but on an interface

from abc import abstractmethod


class xyz:
    @abstractmethod
    def bake(self):
        raise NotImplementedError

    @abstractmethod
    def eat(self):
        raise NotImplementedError


class Bread(xyz):

    def bake(self):
        print("Bread is baked")
    
    def eat(self):
        print("Bread is eaten")


class Pizza(xyz):

    def bake(self):
        print("Pizza is baked")
    
    def eat(self):
        print("Pizza is eaten")


class Production():

    def __init__(self, food) -> None:
        self.food = food

    def produce(self):
        self.food.bake()
    
    def comsume(self):
        self.food.eat()



if __name__ == "__main__":
    bread = Bread()
    pizza = Pizza()
    prod1 = Production(bread)
    prod2 = Production(pizza)
    prod1.produce()
    prod1.comsume()
    

    