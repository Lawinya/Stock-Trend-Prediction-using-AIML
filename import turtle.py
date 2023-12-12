import turtle

# Create a turtle instance
car = turtle.Turtle()

# Draw the body of the car
car.color("red")
car.fillcolor("red")
car.begin_fill()
car.forward(100)
car.left(90)
car.forward(20)
car.left(90)
car.forward(20)
car.right(90)
car.forward(20)
car.left(90)
car.forward(60)
car.left(90)
car.forward(20)
car.right(90)
car.forward(20)
car.left(90)
car.forward(20)
car.end_fill()

# Position for the wheels
car.penup()
car.goto(25, -10)
car.pendown()

# Draw the wheels
car.color("black")
car.fillcolor("black")
car.begin_fill()
car.circle(10)
car.end_fill()

car.penup()
car.goto(75, -10)
car.pendown()

car.color("black")
car.fillcolor("black")
car.begin_fill()
car.circle(10)
car.end_fill()

# Hide the turtle
car.hideturtle()

# Exit on click
turtle.done()
