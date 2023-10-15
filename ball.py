import random
from turtle import *

starting_ball_speed = 1.3
BALL_WIDTH = 2
BALL_LENGTH = 2


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.shapesize(stretch_wid=BALL_WIDTH, stretch_len=BALL_LENGTH)
        self.penup()
        self.move_in_x = 10
        self.move_in_y = 10
        self.BALL_SPEED = starting_ball_speed


    # not used here ,use this to chose random direction of ball while start
    def start(self):
        a = [50, -250]
        self.goto(xcor() + random.choice(a), ycor() + random.choice(a))

    def move(self):
        X = self.xcor() + self.move_in_x
        Y = self.ycor() + self.move_in_y
        self.speed(self.BALL_SPEED)
        self.goto(X, Y)

    def bounce(self):
        self.move_in_y *= -1

    def paddle_bounce(self):
        self.move_in_x *= -1
        self.BALL_SPEED += 0.2

    def restart(self):
        self.BALL_SPEED = starting_ball_speed
        self.goto(0, 0)
        self.move_in_x *= -1
