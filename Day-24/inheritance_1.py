class Animals:
    def __init__(self,name):
        self.name = name
    def output(self):
        print("Animal name : ",self.name)    
class Dog(Animals):
    def sound(self):
        print(self.name,"is barking Bhow bhow")
d = Dog("Suraj")
d.output()
d.sound()