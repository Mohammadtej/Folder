import time

class car:
    def __init__(self,color,speed):
        self.color = color

def crash(car1, car2):
        car1.color = 'burnt'

myCar = car('blue',259)
crash(myCar, car('red', 100))