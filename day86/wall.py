from turtle import Screen
from paddle import Paddle
from wall import Sidewall, Topwall
from ball import Ball
from brick import Brick
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=720, height=1000)
screen.title("BREAKOUT")
screen.tracer(0)

paddle = Paddle()
scoreboard = Scoreboard()
l_sidewall = Sidewall((-355, 0))
r_sidewall = Sidewall((345, 0))
topwall = Topwall((0, 400))
ball = Ball()

brick_x_origin = -324
brick_y_origin = 200

bricks = []
colors = ['yellow', 'yellow', 'green', 'green', 'orange', 'orange', 'red', 'red']
for j in range(8):
    for i in range(14):
        brick = Brick((brick_x_origin, brick_y_origin), colors[j])
        brick.point = 1 + j // 2 * 2
        brick_x_origin += 49
        bricks.append(brick)
    brick_y_origin += 18
    brick_x_origin = -324

screen.listen()
screen.onkeypress(fun=paddle.go_left, key="Left")
screen.onkeypress(fun=paddle.go_right, key="Right")

game_is_on = True
red_brick_broken = 0
orange_brick_broken = 0
paddle_size = 60
n_hit = 0

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if not bricks or scoreboard.ball == 0:
        scoreboard.game_end()
        break

    if ball.xcor() > 330 or ball.xcor() < -340:
        ball.bounce_x()

    if ball.ycor() > 380:
        ball.bounce_y()
        paddle.shapesize(stretch_wid=0.7, stretch_len=2.5)
        paddle_size = 30

    if ball.ycor() < -500:
        ball.reset_position()
        paddle.reset_position()
        scoreboard.lose_ball()

    if ball.ycor() == -385 and abs(ball.xcor() - paddle.xcor()) < paddle_size:
        ball.bounce_y()

    for brick in bricks:
        if abs(ball.ycor() - brick.ycor()) in range(23, 28) and abs(ball.xcor() - brick.xcor()) < 46:
            ball.bounce_y()

            n_hit += 1
            if n_hit == 4:
                ball.move_speed *= 0.8
            if n_hit == 12:
                ball.move_speed *= 0.8
            if brick.point == 5 and orange_brick_broken == 0:
                if not orange_brick_broken:
                    ball.move_speed *= 0.8
                    orange_brick_broken += 1
            if brick.point == 7 and red_brick_broken == 0:
                if not red_brick_broken:
                    ball.move_speed *= 0.8
                    red_brick_broken += 1
            brick.hideturtle()
            scoreboard.point(brick.point)
            bricks.remove(brick)

        elif abs(ball.xcor() - brick.xcor()) in range(33, 38) and abs(ball.ycor() - brick.ycor()) < 24:
            ball.bounce_x()

            n_hit += 1
            if n_hit == 4:
                ball.move_speed *= 0.8
            if n_hit == 12:
                ball.move_speed *= 0.8
            if brick.point == 5 and orange_brick_broken == 0:
                if not orange_brick_broken:
                    ball.move_speed *= 0.8
                    orange_brick_broken += 1
            if brick.point == 7 and red_brick_broken == 0:
                if not red_brick_broken:
                    ball.move_speed *= 0.8
                    red_brick_broken += 1
            brick.hideturtle()
            scoreboard.point(brick.point)
            bricks.remove(brick)

screen.exitonclick()