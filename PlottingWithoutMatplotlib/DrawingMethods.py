import turtle
import pandas
import numpy
from Plot import Plot


drawer = turtle.Turtle()

turtle.setworldcoordinates(-100, -100, 1100, 1100)
turtle.hideturtle()
ticks = numpy.arange(0,1001,100)

fakeMin = -5
fakeMax = 40

myPlot = Plot()


def drawRectangle(x, y, height, width):


    setCoordinates(x,y)

    if height > 0:
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
    else:
        height = abs(height)

        turtle.pd()
        turtle.seth(0)
        turtle.begin_fill()

        #top
        turtle.forward(width)
        turtle.right(90)

        #right
        turtle.forward(height)
        turtle.right(90)

        #bottom
        turtle.forward(width)
        turtle.right(90)

        #left
        turtle.forward(height)
        turtle.right(90)

        turtle.end_fill()

def setCoordinates(x,y):
    turtle.pu()
    turtle.setx(x)
    turtle.sety(y)

def drawAxisY():
    setCoordinates(0,0)
    
    turtle.pd()
    turtle.seth(90)
    turtle.forward(1000)

def drawTicks(ticksList):
    
    
    for height in ticksList:
        setCoordinates(-15,height)
        turtle.pd()
        turtle.seth(0)
        turtle.forward(30)

def labelTicks(min, max):

    range = abs(min)+abs(max)
    increment = range * .1

    labels = numpy.arange(min,max+1,increment)

    height = -12
    for label in labels:
        setCoordinates(-50,height)
        turtle.pd()
        turtle.seth(0)
        turtle.write(str(label))
        height += 100

def drawAxisX(height):
    
    
    setCoordinates(0, height)
    turtle.pd()
    turtle.seth(0)
    turtle.forward(1000)


drawAxisY()
drawTicks(ticks)
labelTicks(-5,40)
drawAxisX(myPlot.xAxisHeight)

iterator = 0

while iterator < myPlot.xSeries.count():
    x = myPlot.locations[iterator]
    y = myPlot.xAxisHeight
    height = myPlot.xSeries[iterator]
    height = (height/myPlot.rangey*1000)
    drawRectangle(x, y, height, 30)
    iterator += 1

turtle.done()





    
