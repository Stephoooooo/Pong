from turtle import Turtle
FONT = ('Arial', 88, 'normal')
ALIGNMENT = 'center'

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.color("white")
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)

    def left_point(self):
        self.r_score += 1
        self.update_scoreboard()

    def right_point(self):
        self.l_score += 1
        self.update_scoreboard()