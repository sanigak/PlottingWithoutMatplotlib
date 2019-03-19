import pandas
import numpy

#stores info necessary for generating plot

class Plot:



    #SET FILENAME HERE
    dataset = pandas.read_csv("example.csv")


    ticks = numpy.arange(0,1001,100)

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



    if absMin < 0:
        rangey = abs(absMin)+abs(absMax)
    else:
        rangey = absMax

    def xAxisHeight(min, max):
        if (min>0):
            return 0
        else:
            range = abs(min)+abs(max)
            perc = abs(min)/range
            height = 1000*perc
            return height

    def rectangleStartingX(numberOfItems):
        factor = 900/(numberOfItems-1)
        locations = numpy.arange(15,916,factor)
        return locations


    xAxisHeight = xAxisHeight(absMin,absMax)
    locations = rectangleStartingX(aSeries.count())
    locations2 = locations + 30
    labels = locations + 60




