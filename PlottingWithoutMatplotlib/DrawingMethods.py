import turtle
import pandas
import numpy
from Plot import Plot

#Hello!

#By default, program will read the csv "example.csv" from inside the project directory
#This can be changed in line 11 of Plot.py





#I chose to use turtle for graphics, and pandas and numpy for some matrix manipulation stuff
drawer = turtle.Turtle()


#Set world grid, originally was simply (0,0,1000,1000), but I figured some margins would come in use depending on what labels and other info I wanted to add to the sides later
turtle.setworldcoordinates(-200, -100, 1100, 1100)
turtle.hideturtle()

#I split the project up into 2 files: this DrawingMethods.py and Plot.py
#DrawingMethods.py contains all the methods for drawing, as well as the engine which brings everything together
#Plot.py contains all the abstract info necessary to draw the plot - see file for more details
myPlot = Plot()

turtle.speed = "fastest"


#Takes in coordinates, height, and width, and draws a rectanlge to those specifications at that location
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

#Moves the turtle cursor to a specific coordinate (without drawing a line).  Helper method used in many of the others
def setCoordinates(x,y):
    turtle.pu()
    turtle.setx(x)
    turtle.sety(y)

#Simply draws a verticle line at (0,0)
def drawAxisY():
    setCoordinates(0,0)
    
    turtle.pd()
    turtle.seth(90)
    turtle.forward(1000)


#Adds draws 10 tick marks at even
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
    while iterator < myPlot.aSeries.count():
        rectLabel = categorySeries[iterator]
        x = locations[iterator]+ 70
        
        setCoordinates(x,height)
        turtle.write(rectLabel)

        iterator += 1

def makeRectangles():

    turtle.color("black","red")
    iterator = 0
    while iterator < myPlot.aSeries.count():
        x = myPlot.locations[iterator]
        y = myPlot.xAxisHeight
        height = myPlot.aSeries[iterator]
        height = (height/myPlot.rangey*1000)
        drawRectangle(x, y, height, 30)
        iterator += 1

    turtle.color("black","blue")
    iterator = 0
    while iterator < myPlot.bSeries.count():
        x = myPlot.locations2[iterator]
        y = myPlot.xAxisHeight
        height = myPlot.bSeries[iterator]
        height = (height/myPlot.rangey*1000)
        drawRectangle(x, y, height, 30)
        iterator += 1

def makeKey():

    turtle.color("black","red")
    drawRectangle(-200,500, 30,30)
    setCoordinates(-200,465)
    turtle.write(myPlot.aType)

    turtle.color("black","blue")
    drawRectangle(-200,400, 30,30)
    setCoordinates(-200,365)
    turtle.write(myPlot.bType)

def Engine():

    drawAxisY()

    drawTicks(myPlot.ticks)

    labelTicks(myPlot.absMin, myPlot.absMax)

    drawAxisX(myPlot.xAxisHeight)

    makeRectangles()

    labelAxisX(myPlot.absMin, myPlot.absMax)

    makeKey()

    turtle.done()

Engine()

