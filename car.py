import random

class Car():
    color = "White"
    shape = "🚗"
    time_parked = 0
    def newColor(self):
        colors = ['red', 'green', 'blue', 'yellow']
        self.color = random.choice(colors)

# my_car = Car()

# my_car.newColor()

# print(my_car.color)
