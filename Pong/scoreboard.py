from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.init()



    def init(self):
        self.penup()
        self.score_p1 = 0
        self.score_p2 = 0
        self.color("white")
        self.setpos(0, 240)
        self.speed("fastest")
        self.write(f"{self.score_p1}   {self.score_p2}", False, align="center", font=('Arial', 20))
        self.hideturtle()

    def score_inc_p1(self):
        self.clear()
        self.score_p1 += 1
        self.write(f"{self.score_p1}   {self.score_p2}", False, align="center", font=('Arial', 20))

    def score_inc_p2(self):
        self.clear()
        self.score_p2 += 1
        self.write(f"{self.score_p1}   {self.score_p2}", False, align="center", font=('Arial', 20))

