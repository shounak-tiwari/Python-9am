from abc import ABC , abstractmethod
class Area(ABC):
    @abstractmethod
    def area(self,b,h):
        return (1/2*(b*h)) 

class Triangle(Area):
    def area(self, b, h):
        return super().area(b, h)
    
x = Triangle()
print(x.area(10,20))