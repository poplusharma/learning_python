from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.ball = 3

        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(320, 420)
        self.write(self.score, align="Right", font=("Courier", 60, "normal"))
        self.goto(60, 430)
        self.write("Score: ", align="Left", font=("Courier", 40, "normal"))
        self.goto(-330, 430)
        self.write("Ball: ", align="Left", font=("Courier", 40, "normal"))
        self.goto(-170, 420)
        self.write(self.ball, align="Right", font=("Courier", 60, "normal"))

    def lose_ball(self):
        self.ball -= 1
        self.update_scoreboard()

    def point(self, point):
        self.score += point
        self.update_scoreboard()

    def game_end(self):
        self.goto(0, 0)
        self.write("END", align="Center", font=("Courier", 60, "normal"))
