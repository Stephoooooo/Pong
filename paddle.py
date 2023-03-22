from turtle import Turtle
STARTING_POSITION = (350,0)
MOVE_DISTANCE = 20

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.create_paddle()
        self.goto(position)

    def create_paddle(self):
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1.0)
        self.color("white")
        self.penup()

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)