#!/usr/bin/python3

#Setup imports
import sys
import time

#Setup the Matrix
import smbus
bus = smbus.SMBus(2)
matrix = 0x70
index = [0x80, 0x00, 0x00, 0x00,
     0x00, 0x00, 0x00, 0x00,
     0x00, 0x00, 0x00, 0x00,
     0x00, 0x00, 0x00, 0x00]

bus.write_byte_data(matrix, 0x21, 0)
bus.write_byte_data(matrix, 0x81, 0)
bus.write_byte_data(matrix, 0xe7, 0)

#Setup the encoders
eQEP1 = '1'
eQEP2 = '2'
COUNTERPATH1 = '/dev/bone/counter/' + eQEP1+ '/count0'
COUNTERPATH2 = '/dev/bone/counter/' + eQEP2+ '/count0'

ms = 100
maxCount = '1000000'
#Set the eEQP max count
f = open(COUNTERPATH1+ '/ceiling', 'w')
f.write(maxCount)
f.close()
g = open(COUNTERPATH2+ '/ceiling', 'w')
g.write(maxCount)
g.close()

#Enable
f =  open(COUNTERPATH1+ '/enable', 'w')
f.write('1')
f.close()
g =  open(COUNTERPATH2+ '/enable', 'w')
g.write('1')
g.close()

f =  open(COUNTERPATH1+ '/count', 'r')
g =  open(COUNTERPATH2+ '/count', 'r')

#Keep track of the previous encoder position
olddata1 = -1
olddata2 = -1

#Print instructions
print("Etch-A-Sketch")
print("Move with rotary encoders")
print("Move up: Left encoder CCW")
print("Move down: Left encoder CW")
print("Move right: Right encoder CW")
print("Move left: Right encoder CCW")

#Prompt for row and column numbers
rows = 8
columns = 8

size = width, height = int(500/columns)*columns, int(500/rows)*rows
#Set cursor
cursorleft = 0
cursortop = 0

#Track the row and column of the cursor
cursorCol = 0
cursorRow = 0
  
#Function to move the cursor up
def moveup():
    global cursortop,currRow,index,cursorRow
    #If moving will put it outside of the screen, don't do it
    if (cursortop - height/rows) >= 0:
        #Move the cursor
        cursortop = cursortop - height/rows
        cursorRow = cursorRow - 1

#Function to move the cursor down
def movedown():
    global cursortop,currRow,index,cursorRow
    #If moving will put it outside of the screen, don't do it
    if (cursortop + 2 * height/rows) <= width:
        #Move the cursor
        cursortop = cursortop + height/rows
        cursorRow = cursorRow + 1

#Function to move the cursor right
def moveright():
    global cursorleft,currColumn,index,cursorCol
    #If moving will put it outside of the screen, don't do it
    if (cursorleft + 2 * width/columns) <= width:
        #Move the cursor
        cursorleft = cursorleft + width/columns
        cursorCol = cursorCol + 1

#Function to move the cursor left
def moveleft():
    global cursorleft,currColumn,index,cursorCol
    #If moving will put it outside of the screen, don't do it
    if (cursorleft - width/columns) >= 0:
        #Move the cursor
        cursorleft = cursorleft - width/columns
        cursorCol = cursorCol - 1

#Main loop
while 1:
    f.seek(0)
    g.seek(0)
    data1 = f.read()[:-1]
    data2 = g.read()[:-1]
    #Handle move left
    if int(data1) > int(olddata1):
        olddata1 = data1
        print("data1 left = " + data1)
        moveleft()
        
    #Handle move right
    elif int(data1) < int(olddata1):
        olddata1 = data1
        print("data1 right = " + data1)
        moveright()
    #Handle move down
    elif int(data2) > int(olddata2):
        olddata2 = data2
        print("data2 down = " + data2)
        movedown()
    #Handle move up
    elif int(data2) < int(olddata2):
        olddata2 = data2
        print("data2 up = " + data2)
        moveup()
    time.sleep(ms/1000)

    #Add the cursor position to the column array
    index[(7-cursorCol) * 2] = index[(7-cursorCol) * 2] | (0x01 << cursorRow)
    #Draw the blocks on the matrix
    bus.write_i2c_block_data(matrix, 0, index)
