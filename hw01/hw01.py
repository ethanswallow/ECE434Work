#!/usr/bin/python3

#Setup pygame
import sys, pygame
pygame.init()

#Print instructions
print("Etch-A-Sketch")
print("Move by entering Commands in command line")

#Prompt for row and column numbers
rows = int(input("Enter rows: "))
columns = int(input("Enter columns: "))

#Initialize width and height to be about 500
#Should be exactly divisible by the numer of rows or columns 
width, height = (int(500/columns)*columns, int(500/rows)*rows)
white = (255,255,255)
black = (0,0,0)

#Initialize the screen as a pygame surface
screen = pygame.display.set_mode((width, height))

#Set cursor
cursorleft = 0
cursortop = 0

#Function to move the cursor up
def moveup():
	global cursortop,currRow,index
	#If moving will put it outside of the screen, don't do it
	if (cursortop - height/rows) >= 0:
		#Move the cursor
		cursortop = cursortop - height/rows

#Function to move the cursor down
def movedown():
	global cursortop,currRow,index
#If moving will put it outside of the screen, don't do it
	if (cursortop + 2 * height/rows) <= width:
		#Move the cursor
		cursortop = cursortop + height/rows

#Function to move the cursor right
def moveright():
	global cursorleft,currColumn,index
	#If moving will put it outside of the screen, don't do it
	if (cursorleft + 2 * width/columns) <= width:
		#Move the cursor
		cursorleft = cursorleft + width/columns

#Function to move the cursor left
def moveleft():
	global cursorleft,currColumn,index
	#If moving will put it outside of the screen, don't do it
	if (cursorleft - width/columns) >= 0:
		#Move the cursor
		cursorleft = cursorleft - width/columns

#Function to clear the screen
def clear():
	screen.fill(white)

#Initially clear the screen
screen.fill(white)

#Main loop
while 1:
	#Handle events
	line = input("Enter Command: ")
	#Handle quit
	if line =='e':
		sys.exit()
	#Handle UP arrow
	elif line =='u':
		moveup()
	#HAndle DOWN arrow
	elif line == 'd':
		movedown()
	#Handle right arrow
	elif line == 'r':
		moveright()
	#Handle left arrow
	elif line == 'l':
		moveleft()
	#Handle SPACEBAR
	elif line == 'c':
		clear()

	#Draw the rectangle based on where the cursor is
	pygame.draw.rect(screen,black,(cursorleft,cursortop,width/columns,height/rows))

	#Update the screen
	pygame.display.update()
