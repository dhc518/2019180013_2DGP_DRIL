import turtle
count = 0
x = 100
y = 100

turtle.penup(); turtle.goto(0,-100 );turtle.pendown()

while count < 6 :
    turtle.goto(500, y * count-100)
    turtle.penup()
    count += 1
    turtle.goto(0, y * count -100)
    turtle.pendown()

turtle.penup(); turtle.goto(0, -100);turtle.pendown()
count = 0

while count < 6 :
    turtle.goto(x * count, 400)
    turtle.penup()
    count += 1
    turtle.goto(x * count, -100)
    turtle.pendown()

turtle.exitonclick()
