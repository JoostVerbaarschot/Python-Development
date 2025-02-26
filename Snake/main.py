import turtle as t
import snake as s
import food as f
import scoreboard as sb
import time




t.colormode(255)
screen = t.Screen()

screen.setup(600,600)
screen.bgcolor("black")
screen.title("snek")
screen.tracer(0)

snake = s.Snake()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.ri, "d")
screen.onkey(snake.down, "s")
screen.onkey(snake.le, "a")

apple = f.Food()
scoreb= sb.ScoreBoard()


def eating():
    if snake.head.distance(apple) < 15:
        apple.refresh()
        scoreb.score_inc()
        snake.addseg()

def boundary():
    return snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280

def tail_col():
    for seg in snake.s_seg[1:]:  # Skip the head (index 0)
        if snake.head.distance(seg) < 10:  # Check if head is too close to a segment
            return True
    return False  


running = bool(True)
while running:
    screen.update()
    time.sleep(0.1)


    snake.update()
    eating()

    if tail_col() or boundary():
        running = False
        print("GameOver")

screen.exitonclick()

