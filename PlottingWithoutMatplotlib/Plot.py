import pandas
import numpy

#Stores info necessary for generating plot

#I realize that a more typical OO design would involve initializing the object with self-referentail methods, but since the object that we are creating here is used only once...
#...and will be static after creation, this design works.  If the project specs had been different I might've designed this to allow for more dynamic usage.

class Plot:



    #SET FILENAME HERE
    dataset = pandas.read_csv("example.csv")

    #Array for where the Y axis tick marks should go
    ticks = numpy.arange(0,1001,100)




    #This section uses pandas to parse the csv files into convenient objects
    columns = dataset.columns

    categoryType = columns[0]
    aType = columns[1]
    bType = columns[2]


    categorySeries = dataset[categoryType]
    aSeries = dataset[aType]
    bSeries = dataset[bType]


    aMin = aSeries.min()
    aMax = aSeries.max()
    bMin = bSeries.min()
    bMax = bSeries.max()


    #Determing the max and min of the 2 numerical fields combined
    absMin = 0
    absMax = 0
    if (aMin < bMin):
        absMin = aMin
    else:
        absMin = bMin

    if (aMax > bMax):
        absMax = aMax
    else:
        absMax = bMax


    #Calculates the total range from absMin to absMax
    if absMin < 0:
        rangey = abs(absMin)+abs(absMax)
    else:
        rangey = absMax


    #Takes in min and max, and calculates the height of the x axis
    def xAxisHeight(min, max):
        if (min>0):
            return 0
        else:
            range = abs(min)+abs(max)
            perc = abs(min)/range
            height = 1000*perc
            return height

    #Determines the X values of the starting locations for the bars
    def rectangleStartingX(numberOfItems):
        factor = 900/(numberOfItems-1)
        locations = numpy.arange(15,916,factor)
        return locations


    xAxisHeight = xAxisHeight(absMin,absMax)
    locations = rectangleStartingX(aSeries.count())
    locations2 = locations + 30
    labels = locations + 60




