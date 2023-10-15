from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.left_player_score = 0
        self.right_player_score = 0
        self.goto(0, 300)
        self.write(arg="SCORES", align="center", font=("Arial", 25, "normal"))
        self.goto(-150, 300)
        self.write(arg=f"{self.left_player_score}", align="center", font=("Arial", 25, "normal"))
        self.goto(150, 300)
        self.write(arg=f"{self.right_player_score}", align="center", font=("Arial", 25, "normal"))

    def update_score(self):
        self.goto(0, 300)
        self.write(arg="SCORES", align="center", font=("Arial", 25, "normal"))
        self.goto(-150, 300)
        self.write(arg=f"{self.left_player_score}", align="center", font=("Arial", 25, "normal"))
        self.goto(150, 300)
        self.write(arg=f"{self.right_player_score}", align="center", font=("Arial", 25, "normal"))

    def update_left_score(self):
        self.clear()
        self.left_player_score += 1
        self.update_score()

    def update_right_score(self):
        self.right_player_score += 1
        self.clear()
        self.update_score()
