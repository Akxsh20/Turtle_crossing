import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player=Player()
car_manager = CarManager()
scoreboard =Scoreboard()



screen.onkey(player.move,"Up")

game_is_on = True
while game_is_on:
    time.sleep(.1)
    screen.update()
    car_manager.create()
    car_manager.move()
    if player.ycor() > 280 :
        player.reset()
        car_manager.level_up()
        print("Level up")
        scoreboard.current_score()

    for car in car_manager.car_list:
        if car.distance(player) < 20:
            game_is_on=False
            scoreboard.game()

screen.exitonclick()
