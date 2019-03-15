import pandas
import numpy

#stores info necessary for generating plot

class Plot:


    dataset = pandas.read_csv("example.csv")

    columns = dataset.columns

    categoryType = columns[0]
    xType = columns[1]


    categorySeries = dataset[categoryType]
    xSeries = dataset[xType]


    xMin = xSeries.min()
    xMax = xSeries.max()

    if xMin < 0:
        rangey = abs(xMin)+abs(xMax)
    else:
        rangey = xMax

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


    xAxisHeight = xAxisHeight(xMin,xMax)
    locations = rectangleStartingX(xSeries.count())




