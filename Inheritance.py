#Inheritance is an OOP concept that allows a child class/derived class to inherit properties of a parent class
class Animal:
    def __init__(self,color,age,weight):
        self.color=color
        self.age=age
        self.weight=weight
    def output(self):
        print(self.color,self.age,self.weight)
class domestic_Animal(Animal):
    #domestic_Animal is a child class
    pass
#pass allows the derived class to inherit properties of the main class
cow=domestic_Animal("black",10,70)
print(cow.output())

#Python collections include
#Set-{}
#Tuple-()
#Dictionary={}
#List - []
#Array - []

#Inheritance, encapsulation, abstraction, polymorphism

