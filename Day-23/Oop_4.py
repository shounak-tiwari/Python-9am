class Demo:
    def __new__(cls):
        return super.__new__()
    def __init__(self):
        self.name = input("Enter the name of student : ")
    def output(self):
        print(self.name)
Demo()