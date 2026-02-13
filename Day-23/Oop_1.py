# instance : it use for track current active object 
class Animal:
    # behaviour of function 
    def InputDetails(self):
        self.Name = str(input("Enter the name : "))
    def OutputDetails(self):
        print(f"The name of Animal : {self.Name}")
# create object - 1
Human,Dogesh = Animal(),Animal()
Human.InputDetails()
Human.OutputDetails()
Dogesh.InputDetails()
Dogesh.OutputDetails()