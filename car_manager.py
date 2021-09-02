from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
STARTING_X=280



class CarManager:
    def __init__(self):
        self.car_list=[]
        self.speed=STARTING_MOVE_DISTANCE

    def create(self):
        chance=random.randint(1,6)
        if chance == 1:
            car=Turtle("square")
            car.penup()
            car.shapesize(stretch_wid=1,stretch_len=2)
            car.color(random.choice(COLORS))
            car.setposition(STARTING_X, random.randint(-230, 280))
            self.car_list.append(car)

    def move(self):
        for car in self.car_list:
            car.backward(self.speed)

    def level_up(self):
        self.speed+=MOVE_INCREMENT