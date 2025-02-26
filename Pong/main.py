import turtle as t
import scoreboard as sb
import midline as ml
import time
import player as p
import ball as b


t.colormode(255)
screen = t.Screen()

screen.setup(800,600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


screen.listen()

scoreb = sb.ScoreBoard()

midl = ml.MidLine()
p1 = p.Player(-350)
p2 = p.Player(350)
ball = b.Ball()

screen.onkey(p1.up, "w")
screen.onkey(p1.down, "s")
screen.onkey(p2.up, "Up")
screen.onkey(p2.down, "Down")

def collision(self):
    print(f"Distance :{ball.distance(self)}")
    print(f"x cordinate :{ball.pos()}")
    if ball.distance(self) < 45 and ball.xcor() > 320 or ball.distance(self) < 45 and ball.xcor() < -320:
        return True

def wall_collision(self):
    if self.ycor() > 285 or self.ycor() < -285:
        return True

def missed():
    if ball.xcor() > 360:
        return 1
    if ball.xcor() < -360:
        return 2

running = bool(True)
while running:
    screen.update()
    time.sleep(0.1)
    ball.move()

    if wall_collision(ball):
        ball.on_col_wall()

    if collision(p1) or collision(p2):
        print("collision")
        ball.on_col_paddle()

    if missed() == 1:
        scoreb.score_inc_p1()
        ball.refresh(-10)
    if missed() == 2:
        scoreb.score_inc_p2()
        ball.refresh(10)

screen.exitonclick()
