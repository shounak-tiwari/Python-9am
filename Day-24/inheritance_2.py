class Animals:
    def __init__(self,name):
        self.name = name
    def output(self):
        print("Animal name : ",self.name)    
class Dog(Animals):
    def __init__(self,name,breed):
        super().__init__(name)#call parent constructor 
        self.breed = breed
    def sound(self):
        print(self.name,"is barking Bhow bhow")
    def details(self):
        print(f"Name of dog is {self.name} and breed is {self.breed}")

d = Dog("Suraj","Indian")
d.output()
d.sound()
d.details()