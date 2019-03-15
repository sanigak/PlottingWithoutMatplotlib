import turtle
import pandas
import numpy
from Plot import Plot


drawer = turtle.Turtle()

turtle.setworldcoordinates(-100, -100, 1100, 1100)
turtle.hideturtle()
ticks = numpy.arange(0,1001,100)

myPlot = Plot()

turtle.speed = "fastest"

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
    
    if min < 0:
        range = abs(min)+abs(max)
    else:
        range = max

    increment = range * .1

    if min < 0:
        labels = numpy.arange(min,max+1,increment)
    else:
        labels = numpy.arange(0,max+1,increment)

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

def labelAxisX(min, max):


    if min < 0:
        range = abs(min)+abs(max)
    else:
        range = max

    categorySeries = myPlot.categorySeries
    locations = myPlot.locations
    height = myPlot.xAxisHeight + 5

    increment = range * .1

    if min < 0:
        labels = numpy.arange(min,max+1,increment)
    else:
        labels = numpy.arange(0,max+1,increment)
    
    print(labels)
    labels += 30
    print(labels)

    iterator = 0
    while iterator < myPlot.xSeries.count():
        rectLabel = categorySeries[iterator]
        x = locations[iterator]+ 40
        
        setCoordinates(x,height)
        turtle.write(rectLabel)

        iterator += 1

def labelAxisY():
    setCoordinates(-100,450)
    turtle.pd()
    turtle.seth(90)
    turtle.write(myPlot.xType, font=("Arial", 10, "bold"))    

def makeRectangles():
    iterator = 0
    while iterator < myPlot.xSeries.count():
        x = myPlot.locations[iterator]
        y = myPlot.xAxisHeight
        height = myPlot.xSeries[iterator]
        height = (height/myPlot.rangey*1000)
        drawRectangle(x, y, height, 30)
        iterator += 1

def Engine():

    drawAxisY()

    drawTicks(ticks)

    labelTicks(myPlot.xMin, myPlot.xMax)

    drawAxisX(myPlot.xAxisHeight)

    makeRectangles()

    labelAxisX(myPlot.xMin, myPlot.xMax)

    labelAxisY()

    turtle.done()

Engine()

