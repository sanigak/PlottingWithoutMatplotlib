import turtle
import pandas


drawer = turtle.Turtle()

turtle.setworldcoordinates(0, 0, 1000, 1000)

def drawRectangle(height, width):
    turtle.pd()
    turtle.seth(0)
    turtle.begin_fill()

    #bottom
    turtle.forward(width)
    turtle.left(90)

    #right
    turtle.forward(height)
    turtle.left(90)

    #top
    turtle.forward(width)
    turtle.left(90)

    #left
    turtle.forward(height)
    turtle.left(90)

    turtle.end_fill()


def setCoordinates(x,y):
    turtle.pu()
    turtle.setx(x)
    turtle.sety(y)


def drawAxes():
    setCoordinates(10,10)
    turtle.pd()
    turtle.forward(900)
    setCoordinates(10,10)
    turtle.pd()
    turtle.left(90)
    turtle.forward(900)

#drawAxes()
#setCoordinates(20,20)
#drawRectangle(200,30)
#turtle.done()


