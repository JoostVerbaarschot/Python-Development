from turtle import Turtle

class Player(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.init(pos)

    def init(self,pos):
            self.setpos(pos, 0)
            self.penup()
            self.color("white")
            self.shapesize(1,5)
            self.speed("fastest")
            self.shape("square")
            self.setheading(90)



    def up(self):
        self.goto(self.xcor(),self.ycor() + 20)

    def down(self):
        self.goto(self.xcor(),self.ycor() - 20)

