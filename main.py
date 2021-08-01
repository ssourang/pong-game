from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time


screen = Screen()
ball = Ball()
score = Score()

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)

screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong')
screen.tracer(0)

screen.listen()
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')

try:
    game_is_on = True
    while game_is_on:
        time.sleep(ball.move_speed)
        screen.update()
        ball.move()

        # Detect collision with wall
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.y_bounce()

        # Detect collision with paddle
        if r_paddle.distance(ball) < 50 and ball.xcor() > 320 or l_paddle.distance(ball) < 50 and ball.xcor() < -320:
            ball.x_bounce()
            # if speed < 10:
            #     ball.speed(speed+1)

        # Detect when right paddle misses
        if ball.xcor() > 380:
            ball.reset_position()
            score.l_point()

        # Detect when left paddle misses
        if ball.xcor() < -380:
            ball.reset_position()
            score.r_point()


    screen.exitonclick()
except:
    print('Game closed!')