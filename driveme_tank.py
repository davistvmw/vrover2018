##Using Python 2.7.3

import RPi.GPIO as gpio
import time
import sys

#Goal: Drive vechicle using Remote Control including:
## ---driveme.init() --- Initialise GPIO pins to drive as output
## ---driveme.forward(tf) --- Drive Foward
## ---driveme.reverse --- Drive in Reverse
## ---driveme.turn_left_fwd --- Turn left while moving forward
## ---driveme.turn_right_fwd --- Turn right while moving forward
## ---driveme.turn_left_rev --- Turn left while moving backward
## ---driveme.turn_right_rev --- Turn right while moving backward
## ---driveme.pivot_right --- Pivot clockwise (defined as from a 'birds eye view' with 12o'clock at the front of the vehicle (Pivot right)
## ---driveme.pivot_left --- Pivot counter clockwise (Pivot left)

#Assumption: All right and all left wheels drive together.
#Refer to test image - colour is lead colour. GPIO input defined in variables:
#Blue Lead goes to right front wheel and back right wheel - forward spin (rt_fwd) - green LEDs
#White lead goes to right front wheel and right back wheel - reverse spin (rt_rev) - red LEDs

#Purple Lead goes to left front wheel and left back wheel - forward spin (lft_fwd) - yellow LEDs
#Yellow lead goes to left front wheel and left back wheel - reverse spin (lft_rev) - red LEDs

##Define variables for each wheel to map to the GPIO pin output. Replace variables with the corresponding GPIO pin on your rover.
## modified by KD - added enable code

rt_fwd = 22
rt_rev = 18
rt_ena = 16
lft_fwd = 13
lft_rev = 15
lft_ena = 11

##Set up GPIO pins as output
def init():
    try:
        print("Initialising GPIO Pins")
        gpio.setmode(gpio.BOARD)
        gpio.setup(rt_fwd, gpio.OUT)
        gpio.setup(rt_rev, gpio.OUT)
        gpio.setup(rt_ena, gpio.OUT)
        gpio.setup(lft_fwd, gpio.OUT)
        gpio.setup(lft_rev, gpio.OUT)
        gpio.setup(lft_ena, gpio.OUT)
    except:
        print("Your GPIO pins are not set up\n")
##    rt_ena_pwm = gpio.PWM(rt_ena, 1000)
##    lft_ena_pwm = gpio.PWM(lft_ena, 1000)
##    rt_ena_pwm.start(25)
##    lft_ena_pwm.start(25)

##Define a function that will drive the vechicle forward for an amount of time (tf)
def forward(tf):
    try:
        print("Driving forward")
        init()
        gpio.output(rt_ena, True)
        gpio.output(rt_fwd, True)
        gpio.output(rt_rev, False)
        gpio.output(lft_ena, True)
        gpio.output(lft_fwd, True)
        gpio.output(lft_rev, False)
        time.sleep(tf)
        gpio.cleanup()
    except:
        print("Forward virtual: couldn't find wheels to drive\n")

##Define a function that will drive the vechicle in reverse for an amount of time (tf)
def reverse(tf):
    try:
        print("Driving in reverse")
        init()
        gpio.output(rt_ena, True)
        gpio.output(rt_fwd, False)
        gpio.output(rt_rev, True)
        gpio.output(lft_ena, True)
        gpio.output(lft_fwd, False)
        gpio.output(lft_rev, True)
        time.sleep(tf)
        gpio.cleanup()

    except:
        print("Reverse virtual: couldn't find wheels to drive\n")

##Define a function that will drive the vechicle forward and left for an amount of time (tf)
def turn_left_fwd(tf):
    try:
        print("Driving left and forward")
        init()
        gpio.output(rt_ena, True)
        gpio.output(rt_fwd, True)
        gpio.output(rt_rev, False)
        gpio.output(lft_ena, False)
        gpio.output(lft_fwd, False)
        gpio.output(lft_rev, False)
        time.sleep(tf)
        gpio.cleanup()
    except:
        print("Forward left virtual: couldn't find wheels to drive\n")
##Define a function that will drive the vechicle forward and right for an amount of time (tf)
def turn_right_fwd(tf):
    try:
        print("Driving right and forward")
        init()
        gpio.output(rt_ena, False)
        gpio.output(rt_fwd, False)
        gpio.output(rt_rev, False)
        gpio.output(lft_ena, True)
        gpio.output(lft_fwd, True)
        gpio.output(lft_rev, False)
        time.sleep(tf)
        gpio.cleanup()
    except:
        print("Forward right virtual: couldn't find wheels to drive\n")

##Define a function that will drive the vechicle in reverse and left for an amount of time (tf)
def turn_left_rev(tf):
    try:
        print("Driving left in reverse")
        init()
        gpio.output(rt_ena, True)
        gpio.output(rt_fwd, False)
        gpio.output(rt_rev, True)
        gpio.output(lft_ena, False)
        gpio.output(lft_fwd, False)
        gpio.output(lft_rev, False)
        time.sleep(tf)
        gpio.cleanup()
    except:
        print("Reverse left virtual: couldn't find wheels to drive\n")
##Define a function that will drive the vechicle forward and right for an amount of time (tf)
def turn_right_rev(tf):
    try:
        print("Driving right in reverse")
        init()
        gpio.output(rt_ena, False)
        gpio.output(rt_fwd, False)
        gpio.output(rt_rev, False)
        gpio.output(lft_ena, True)
        gpio.output(lft_fwd, False)
        gpio.output(lft_rev, True)
        time.sleep(tf)
        gpio.cleanup()
    except:
        print("Reverse right virtual: couldn't find wheels to drive\n")

##Define a function that will pivot the vechicle clockwise (right) for an amount of time (tf)
def pivot_right(tf):
    try:
        print("Pivoting right")
        init()
        gpio.output(rt_ena, True)
        gpio.output(rt_fwd, False)
        gpio.output(rt_rev, True)
        gpio.output(lft_ena, True)
        gpio.output(lft_fwd, True)
        gpio.output(lft_rev, False)
        time.sleep(tf)
        gpio.cleanup()
    except:
        print("Pivot right virtual: couldn't find wheels to drive\n")

##Define a function that will pivot the vechicle counter-clockwise (left) for an amount of time (tf)
def pivot_left(tf):
    try:
        print("Pivoting left")
        init()
        gpio.output(rt_ena, True)
        gpio.output(rt_fwd, True)
        gpio.output(rt_rev, False)
        gpio.output(lft_ena, True)
        gpio.output(lft_fwd, False)
        gpio.output(lft_rev, True)
        time.sleep(tf)
        gpio.cleanup()
    except:
        print("Reverse left virtual: couldn't find wheels to drive\n")
