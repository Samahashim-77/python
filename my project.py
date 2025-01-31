class Car :
    def __init__(self, make, model, color, price):
        print("calling constructor method...")
        self.make = make
        self.model = model
        self.color = color
        self.price = price
        self.is_running = False
        self.speed = 0


    def start(self):
        self.is_running = True
    print("The car engine is running")

    def stop(self):
        self.is_running = False
        self.speed = 0
        print("The car engine is stopped")

    def accelerate(self, kph):
        self.speed += kph
        print(f"the car is now moving at {self.speed} kph")
        
car1 = Car("Toyota", "Corolla", "Blue", 30000)
print(car1.model, car1.color)
print(car1.is_running)
car1.start()
print(car1.is_running)
car1.accelerate(20)
car1.accelerate(30)
car1.stop()
print(car1.speed)
print(car1.is_running)









 

          