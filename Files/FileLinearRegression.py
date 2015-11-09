# Nathnael Alemu
# Lease squares fit regression line

import turtle
import os.path

def getXcoords(pointList):
    return [p[0] for p in pointList]

def getYcoords(pointList):
    return [p[1] for p in pointList]

def leastSquares(pointList):
    ''' Find the values of m and b for the
    least squares fit regression line for the data points in pointList.
    Return m and b as the tuple m, b'''
    sumOfProduct = 0
    xSum = 0
    ySum = 0
    sumOfSquare = 0
    for point in pointList:
        x = point[0]
        y = point[1]
        sumOfProduct += x*y
        xSum += x
        ySum += y
        sumOfSquare += x**2
    productOfSum = xSum*ySum
    squareOfSum = xSum**2
    m = (len(pointList)*sumOfProduct - productOfSum)/(len(pointList)*sumOfSquare - squareOfSum)
    b = (sumOfSquare*ySum - xSum*sumOfProduct)/(len(pointList)*sumOfSquare - squareOfSum)
    return m, b

def plotPoints(t, pointList):
    ''' Use the turtle t to plot the points in pointList '''
    t.hideturtle()
    t.penup()
    t.color("red")
    
    for p in pointList:
        t.goto(p)
        t.pendown()
        t.goto(p)
        t.dot(5)
        t.penup()

def plotLine(t, m, b, xmin, xmax):
    ''' Use the turtle t to plot the line y = m x + b on the domain [xmin, xmax]'''
    t.color("blue")
    t.width(2.5)
    
    
    t.penup()
    t.goto(xmin,m*xmin+b)
    t.pendown()
    t.goto(xmax,m*xmax+b)
    

def plotErrorBars(t, pointList, m, b):
    ''' Use the turtle t to plot in red a vertical line from each point in pointList
    to the line y = mx + b'''
    t.color("red")
    t.width(2.5)
    for point in pointList:
        x = point[0]
        y = point[1]
        t.penup()
        t.goto(x,y)
        t.pendown()
        t.goto(x,m*x + b)
        t.penup()
        
      
def regression():
    filename = input("Please provide the name of the file including the extention: ")
    while not(os.path.exists(filename)):
        filename = input("Please provide a valid name for the file including the extention: ")
    ds = []
    file = open(filename)
    
    for line in file:
        coordinates = line.split()
        x = float(coordinates[0])
        y = float(coordinates[1])
        point = (x,y)
        ds.append(point)
    my_turtle = turtle.Turtle()
    turtle.title("Least Squares Regression Line")

    
    turtle.clearscreen()
    xmin = min(getXcoords(ds))
    xmax = max(getXcoords(ds))
    ymin = min(getYcoords(ds))
    ymax = max(getYcoords(ds))
    xborder = 0.2*(xmax-xmin)
    yborder = 0.2*(ymax-ymin)
    turtle.setworldcoordinates(xmin-xborder, ymin-yborder, xmax+xborder, ymax+yborder)
    plotPoints(my_turtle, ds)
    m, b = leastSquares(ds)
    print("The equation of the line is y=%fx+%f"%(m,b))
    plotLine(my_turtle, m, b, xmin, xmax)
    plotErrorBars(my_turtle, ds, m, b)
    print("Goodbye")
def main():
    regression()

main()
