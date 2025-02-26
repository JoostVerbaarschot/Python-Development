from turtle import Turtle

class MidLine(Turtle):
    def __init__(self):
        super().__init__()
        self.linelist = []
        self.init()

    def init(self):
        for l in range(-300, 300, 25):
            midl = Turtle()
            self.linelist.append(midl)
            midl.setpos(0, l)
            midl.penup()
            midl.color("white")
            midl.shapesize(0.5, 0.25)
            midl.speed("fastest")
            midl.shape("square")
