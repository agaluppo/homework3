
#NAMES: Alexa Galuppo & Victoria Molitor
#DATE: Feb. 9, 2019
#BUBBLE LEVEL

#Import Statements for microbit and math library commands
from microbit import *
import math

#Defining function that calculates and returns the tilt in the x-axis measured in degrees
def calcAx(d,e,f):
    Ax = (math.atan2(d, (math.sqrt((e**2)+(f**2)))))*(180/math.pi)
    return Ax

#Defining function that calculates and returns the tilt in the y-axis measured in degrees
def calcAy(g,h,i):
    Ay = (math.atan2(y, (math.sqrt((x**2)+(z**2)))))*(180/math.pi)
    return Ay

#Defining function that causes particular images to be displayed based on the x-axis and y-axis tilt of the bubble level
#Arrows displayed show the user which direction they must tilt the microbit in order to make it flat
def happy(j,k):
    if j <= 10 and j >= -10:
        if k <= 10 and k >= -10:
            display.show(Image.HAPPY) #little to no tilt in both the x-axis and the y-axis causes a smiley face to be displayed
        elif k > 10:
            display.show(Image.ARROW_N) #tilt only downward in the y-axis causes an up arrow to be displayed
        else:
            display.show(Image.ARROW_S) #tilt only upward in the y-axis causes a down arrow to be displayed
    elif j > 10:
        if k <= 10 and k >= -10:
            display.show(Image.ARROW_W) #tilt only to the right in the x-axis causes a left arrow to be displayed
        elif k > 10:
            display.show(Image.ARROW_NW) #tilt both downward in the y-axis and to the right in the x-axis causes a diagnolly up and leftward arrow to be displayed
        else:
            display.show(Image.ARROW_SW) #tilt both upward in the y-axis and to the right in the x-axis causes a diagnolly down and leftward arrow to be displayed
    else:
        if k <= 10 and k >= -10:
            display.show(Image.ARROW_E) #tilt only to the left in the x-axis causes a right arrow to be displayed
        elif k > 10:
            display.show(Image.ARROW_NE) #tilt both downward in the y-axis and to the left in the x-axis causes a diagnolly up and rightward arrow to be displayed
        else:
            display.show(Image.ARROW_SE) #tilt both upward in the y-axis and to the left in the x-axis causes a diagnolly down and rightward arrow to be displayed


#This loop continuously runs the above created functions on the microbit
while True:
    sleep(100)
    x = accelerometer.get_x() #imports neccessary data from microbit
    y = accelerometer.get_y() #imports neccessary data from microbit
    z = accelerometer.get_z() #imports neccessary data from microbit
    a = calcAx(x,y,z) #runs first function to calculate the tilt in the x-axis using above imported data
    b = calcAy(x,y,z) #runs second function to calculate the tilt in the y-axis using above imported data
    print((a, b)) #prints tilt in the x-axis and tilt in the y-axis into repl, can also be seen on the plotter
    happy(a,b) #runs third function that uses above calculated tilts to display corrective images on the microbit