import pandas

dataset = pandas.read_csv("example.csv")

columns = dataset.columns

categoryType = columns[0]
xType = columns[1]
yType = columns[2]

categorySeries = dataset[categoryType]
xSeries = dataset[xType]
ySeries = dataset[yType]



xMin = xSeries.min()
xMax = xSeries.max()

xRange = abs(xMin)+abs(xMax)


buffer = int(xRange * .1)


yAxisList = []
marker = xMin-buffer
while marker < xMax:
    yAxisList.append(marker)
    marker += buffer


for item in yAxisList:
    print(item)

rawLine = yAxisList[0]+yAxisList[-1]