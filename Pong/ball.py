from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.y_vel = 0
        self.x_vel = 0
        self.init()
    def init(self):
            self.setpos(0, 0)
            self.penup()
            self.color("white")
            self.speed("fastest")
            self.shape("square")
            print("ball")
            self.y_vel = 10
            self.x_vel = 10
    def move(self):
        next_x = self.xcor() + self.x_vel
        next_y = self.ycor() + self.y_vel
        self.setpos(next_x, next_y)
    def on_col_paddle(self):
        self.x_vel *= -random.uniform(1.1,1.5)
        self.y_vel *= -random.uniform(1.1,1.5)
    def on_col_wall(self):
        self.y_vel *= -1

    def refresh(self, dir):
        self.setpos(0,0)
        self.y_vel = random.randrange(-10,10)
        self.x_vel = dir