from turtle import Turtle

FONT = ("Tahoma", 16, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super(Scoreboard, self).__init__()
        self.color("cyan")
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-260, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align="center", font=FONT)

