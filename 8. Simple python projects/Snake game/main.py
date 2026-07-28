import turtle
import random
import time

# Screen setup
screen = turtle.Screen()
screen.title("Snake Game")
screen.setup(width=700, height=700)
screen.tracer(0)
screen.bgcolor("#786A78")

# Draw border
turtle.speed(5)
turtle.pensize(4)
turtle.penup()
turtle.goto(-310, 250)
turtle.pendown()
turtle.color("red")
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.penup()
turtle.hideturtle()

# Score setup
score = 0
delay = 0.1
score_turtle = turtle.Turtle()
score_turtle.speed(0)
score_turtle.color("white")
score_turtle.penup()
score_turtle.hideturtle()
score_turtle.goto(0, 300)
score_turtle.write("Score: {}".format(score), align="center", font=("Courier", 24, "bold"))

# Snake setup
snake = turtle.Turtle()
snake.speed(0)
snake.shape("circle")
snake.color("green")
snake.penup()
snake.goto(0, 0)
snake.direction = "stop"

# Food setup
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("white")
food.penup()
food.goto(30, 30)

# Snake segments
segments = []

# Movement functions
def snake_go_up():
    if snake.direction != "down":
        snake.direction = "up"

def snake_go_down():
    if snake.direction != "up":
        snake.direction = "down"

def snake_go_left():
    if snake.direction != "right":
        snake.direction = "left"

def snake_go_right():
    if snake.direction != "left":
        snake.direction = "right"

def move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 20)
    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 20)
    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 20)
    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 20)

# Key bindings
screen.listen()
screen.onkeypress(snake_go_up, "Up")
screen.onkeypress(snake_go_down, "Down")
screen.onkeypress(snake_go_left, "Left")
screen.onkeypress(snake_go_right, "Right")

# Main game loop
while True:
    screen.update()

    # Check for food collision
    if snake.distance(food) < 20:
        x = random.randint(-290, 270)
        y = random.randint(-240, 240)
        food.goto(x, y)
        score += 1
        delay -= 0.001

        # Create new snake segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("circle")
        new_segment.color("green")
        new_segment.penup()
        segments.append(new_segment)

        # Update score display
        score_turtle.clear()
        score_turtle.write("Score: {}".format(score), align="center", font=("Courier", 24, "bold"))

    # Move snake segments
    for index in range(len(segments) - 1, 0, -1):
        a = segments[index - 1].xcor()
        b = segments[index - 1].ycor()
        segments[index].goto(a, b)

    if len(segments) > 0:
        a = snake.xcor()
        b = snake.ycor()
        segments[0].goto(a, b)

    move()

    # Check for border collision
    if snake.xcor() > 290 or snake.xcor() < -290 or snake.ycor() > 240 or snake.ycor() < -240:
        time.sleep(1)
        screen.clear()
        screen.bgcolor("turquoise")
        score_turtle.clear()
        score_turtle.goto(0, 0)
        score_turtle.write("   Game Over \n  Your score is :{}".format(score), align="center", font=("Courier", 30, "bold"))
        break

    # Check for body collision
    for segment in segments:
        if snake.distance(segment) < 20:
            time.sleep(1)
            screen.clear()
            screen.bgcolor("turquoise")
            score_turtle.clear()
            score_turtle.goto(0, 0)
            score_turtle.write("   Game Over \n  Your score is :{}".format(score), align="center", font=("Courier", 30, "bold"))
            break

    time.sleep(delay)

turtle.done()