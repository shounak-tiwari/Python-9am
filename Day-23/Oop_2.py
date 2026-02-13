# if any function or variable create thier memory allocation it is only possible when it call by thier object
#Constructor :  when ever object is declared with class memory automatically constructed 
# 1. __new__ 
# 2. __init__ 

class Demo:
    def __init__(cls):
        cls.name = input("Enter the name ")
    def output(cls):
        print(cls.name)
    
obj1 = Demo()
obj1.output()