#!/usr/bin/python3

#Import GPIO and time
import Adafruit_BBIO.GPIO as GPIO
import time

#Setup pygame
import sys
import numpy as np

#Set up GPIO
buttonUp = "P9_21"
buttonDown = "P9_23"
buttonRight = "P9_26"
buttonLeft = "P9_27"
buttonClear = "P9_30"

GPIO.setup(buttonUp, GPIO.IN)
GPIO.setup(buttonDown, GPIO.IN)
GPIO.setup(buttonRight, GPIO.IN)
GPIO.setup(buttonLeft, GPIO.IN)
GPIO.setup(buttonClear, GPIO.IN)

#Print instructions
print("Etch-A-Sketch")
print("Move and clear with buttons")

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
    print(grid)

#Function to move the cursor and clear the screen
def move(channel):
	global x, y, yMax,xMax, grid, buttonUp, buttonDown, buttonRight, buttonLeft, buttonClear
	#if statement to choose which button was pressed
	if channel == buttonUp:
		y -= 1
		print("Up")
		if y<0:
				y= yMax -1
	elif channel == buttonDown:
		print("Down")
		y += 1
		if y >= yMax:
				y=0
	elif channel == buttonRight:
		print("Right")
		x += 1
		if x >= xMax:
				x=0
	elif channel == buttonLeft:
		x -= 1
		print('Left!')
		if x<0:
			x = xMax -1
	elif channel == buttonClear:
		print("Clear")
		grid = np.full((xMax,yMax),' ')

	printGrid(grid)

#Add event Listeners
GPIO.add_event_detect(buttonUp, GPIO.FALLING, callback=move)
GPIO.add_event_detect(buttonDown, GPIO.FALLING, callback=move)
GPIO.add_event_detect(buttonRight, GPIO.FALLING, callback=move)
GPIO.add_event_detect(buttonLeft, GPIO.FALLING, callback=move)
GPIO.add_event_detect(buttonClear, GPIO.FALLING, callback=move)

while 1:
	line = input("Enter Command: ")
	if line == 'e':
		sys.exit()
