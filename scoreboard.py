from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level_number = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 250)
        self.write(arg=f"Level: {self.level_number}", align="center", font=FONT)

    def incremenet_level(self):
        self.level_number += 1
        self.update_scoreboard()
