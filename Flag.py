import turtle

# set up the turtle screen
screen = turtle.Screen()
screen.setup(600, 400)
screen.title("Indian National Flag")
screen.bgcolor("#00BFFF")

# create a turtle object
t = turtle.Turtle()
t.speed(5)
t.hideturtle()

# draw the saffron color
t.penup()
t.goto(-250, 150)
t.pendown()
t.begin_fill()
t.color("black")
for i in range(2):
    t.forward(500)
    t.right(90)
    t.forward(100)
    t.right(90)
t.color("#FF9933")
t.end_fill()

# draw the white color
t.penup()
t.goto(-250, 50)
t.pendown()
t.begin_fill()
t.color("black")
for i in range(2):
    t.forward(500)
    t.right(90)
    t.forward(100)
    t.right(90)
t.color("white")
t.end_fill()

# draw the green color
t.penup()
t.goto(-250, -50)
t.pendown()
t.begin_fill()
t.color("black")
for i in range(2):
    t.forward(500)
    t.right(90)
    t.forward(100)
    t.right(90)
t.color("#138808")
t.end_fill()

# draw the blue wheel
t.penup()
t.goto(0,-50)
t.pendown()
t.color("navy")
t.circle(50)
t.penup()
t.goto(0,-50)
t.pendown()
t.color("navy")
t.circle(49.5)

# draw the 24 spokes of the wheel
t.penup()
t.goto(0, 0)
t.pendown()
t.color("navy")
for i in range(24):
    t.forward(50)
    t.backward(50)
    t.left(15)

# hide the turtle
t.hideturtle()

# exit on click
turtle.exitonclick()
