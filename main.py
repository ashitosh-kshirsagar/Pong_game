from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

my_screen = Screen()
my_screen.bgcolor("black")
my_screen.setup(width=1200, height=700)
my_screen.title("PONG GAME")
my_screen.listen()

left_paddle = Paddle(-550, 0)
right_paddle = Paddle(550, 0)
ball = Ball()
scoreboard = Scoreboard()

my_screen.onkey(key="w", fun=left_paddle.move_up)
my_screen.onkey(key="s", fun=left_paddle.move_down)
my_screen.onkey(key="Up", fun=right_paddle.move_up)
my_screen.onkey(key="Down", fun=right_paddle.move_down)

game_is_on = True
while game_is_on:
    ball.move()

    if ball.xcor() > 565:
        scoreboard.update_left_score()
        ball.restart()

    elif ball.xcor() < -570:
        scoreboard.update_right_score()
        ball.restart()

    elif ball.ycor() > 320 or ball.ycor() < -320:
        ball.bounce()

    elif (right_paddle.distance(ball) < 80 and ball.xcor() > 525) or (left_paddle.distance(ball) < 80 and
                                                                      ball.xcor() < -525):
        ball.paddle_bounce()

my_screen.exitonclick()
