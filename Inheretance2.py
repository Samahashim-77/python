class person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def printall(self):
        print(self.name)
        print(self. age)
        print(self.gender)
class Employee(person):
    def __init__(self, name, age, gender, salary):
        person. __init__(self, name, age, gender)
        self.salary = salary
    def printall(self):
        print(self.name)
        print(self. age)
        print(self.gender)
        print(self.salary)

emp1= Employee("ahmed", 25, "male", 2500)
emp1. printall()
class Manager:
    def __init__(self, name, id, location):
        self.name = name
        self.id = id
        self. location = location
    def printall(self):
        print(self.name)
        print(self.id)
        print(self.location)
class CEO(Employee, Manager):
    def __init__(self, name, id, location, gender, age, salary):
        Manager. __init__(self, name, id, location)
        Employee. __init__(self, name, age, gender, salary)
    def printall(self):
        print(self.name)
        print(self. age)
        print(self.gender)
        print(self.salary)
        print(self. id)
        print(self.location)
ceo1 = CEO("Ali", 3, "Iraq", "Male", 35, 3400)
ceo1.printall()

        
