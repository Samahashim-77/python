class parent(object):
    def __init__(self, name, salary, idnumber):
        self.name = name
        self.salary = salary
        self.idnumber = idnumber
    def display(self):
        print(self.name)
        print(self.salary)
        print(self.idnumber)
    
class child(parent):
    def __init__(self, name, salary, idnumber, height, weight ):
        self.height = height
        self.weight = weight
    #def display1(self,  height, weight):
        #self.height = height
        #self.weight = weight
        super().__init__(self, name, salary,idnumber )
child1= child('sama', 1200, 34, 165, 77)
child1.display()
