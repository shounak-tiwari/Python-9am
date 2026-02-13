class A:
    def __new__(cls):
        print("Creating instance")
        p = super(A, cls).__new__(cls)
        print(id(p))
        return p
    def __init__(self):
        print(id(self))
        self.name  = input("Enter the name of student  : ")
        print("Initializing instance")
        # self.output()
    def output(self):
      	print(self.name)       
A()