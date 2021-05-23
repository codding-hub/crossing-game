from turtle import Turtle
from car_manager import CarManager
from scoreboard import Scoreboard
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("black")
        self.goto_start()
        self.setheading(90)

    def go_up(self):
            self.forward(MOVE_DISTANCE)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
          return True
        else:
            return False

    def goto_start(self):
        self.goto(STARTING_POSITION)






