class circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        print("my area is", 3.14*self.radius*self.radius)
class square:
    def __init__(self, side):
        self.side = side
    def area(self):
        print("my area is", self.side**2)
object1= circle(12)
object2= square(20)
for shape in (object1, object2):
    shape.area()
        
    