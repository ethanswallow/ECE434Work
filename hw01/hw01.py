#!/usr/bin/python3

#Setup numpy and sys
import sys
import numpy as np

#Print instructions
print("Etch-A-Sketch")
print("Move by entering Commands in command line")

#Prompt for row and column numbers
rows = int(input("Enter rows: "))
columns = int(input("Enter columns: "))

xMax = rows
yMax = columns
x = 0
y = 0
grid = np.full((xMax,yMax),' ')
def printGrid(grid):
    grid[x,y] = '+'
    print(x)
    print(y)
    print(grid)
#Main loop
while 1:
    printGrid(grid)
    line = input("Enter Command: ")
    if line =='u':
        y -= 1
        print("Up")
        if y<0:
            y= yMax -1
    elif line == 'd':
        print('Down!');
        y += 1
        if y >= yMax:
            y=0
    elif line == 'l':
        x -= 1
        print('Left!');
        if x<0:
            x = xMax -1
    elif line == 'r':
        print('Right!')
        x += 1
        if x >= xMax:
            x=0
    elif line == 'c':
        print("Clear")
        grid = np.full((xMax,yMax),' ')
    elif line == 'e':
            sys.exit()
            
