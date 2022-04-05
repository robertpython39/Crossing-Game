#-------------------------------------------------------------------------------
# Name:        Crossing Game
# Purpose:     Fun
#
# Author:      nicolescu
#
# Created:     20/03/2022
# Copyright:   (c) nicol 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import time
from turtle import Turtle, Screen
from player import Player
from car_manager import Car_Manager
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.title("Crossing game")
screen.setup(600, 600)
screen.tracer(0)

player = Player()
car = Car_Manager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.going_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_cars()
    car.move_cars()

    # Detect collision with car
    for cr in car.all_cars:
        if cr.distance(player) < 22:
            game_is_on = False
            scoreboard.game_over()

    # Detect succesfull passing
    if player.is_at_finish_line():
        player.go_to_start()
        car.level_up()
        scoreboard.increase_level()

screen.exitonclick()



