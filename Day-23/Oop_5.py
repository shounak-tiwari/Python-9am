class Parameterize:
    def __init__(self,x,y):
        self.new_x = x
        self.new_y = y
    def output(self):
        print(f"the value of x and y is  {self.new_x} and {self.new_y}")
    
obj = Parameterize(10,20)
obj.output()