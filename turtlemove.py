import turtle

turtle.shape("turtle")

def Right():
    turtle.setheading(0)
    turtle.forward(50)
    turtle.stamp()

def Left():
    turtle.setheading(180)
    turtle.forward(50)
    turtle.stamp()

def Up():
    turtle.setheading(90)
    turtle.forward(50)
    turtle.stamp()

def Down():
    turtle.setheading(270)
    turtle.forward(50)
    turtle.stamp()
    
def Clear():
    turtle.clear()
    turtle.penup()
    turtle.goto(0,0)
    turtle.pendown()
    
screen = turtle.Screen()

screen.onkeypress(Right, "Right")
screen.onkeypress(Down, "Down")
screen.onkeypress(Up, "Up")
screen.onkeypress(Left, "Left")
screen.onkeypress(Clear, "Escape")

screen.listen()

screen.mainloop()
