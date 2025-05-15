class Mammal:
    def __init__(self, name, habitat):
        self.name = name
        self.habitat = habitat
    def printdetails (self):
        print(self.name,self.habitat)

class carnivore(Mammal):
    def diet(self):
        return "eats meat"

class herbivore(Mammal):
    def diet(self):
        return "eats plants"


    
fresian=herbivore("cow","domesticated")
fresian.printdetails()
print(fresian.diet())

feline=carnivore("lion","savannah")
feline.printdetails()
print(feline.diet())  