from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong")
screen.bgcolor("black")
screen.tracer(0)


right_paddle = Paddle((350,0))
right_paddle.color("green")
left_paddle = Paddle((-350,0))
left_paddle.color("magenta")
ball = Ball()
scoreboard = Scoreboard()

screen.listen()


screen.onkey(key="Up", fun=right_paddle.up)
screen.onkey(key="Down", fun=right_paddle.down)

screen.onkey(key="w", fun= left_paddle.up)
screen.onkey(key="s", fun=left_paddle.down)

game_is_on = True


while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()


    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()


    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.right_point()



    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.left_point()


screen.exitonclick()
