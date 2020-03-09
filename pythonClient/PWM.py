from __future__ import division
import math
import time

# imprt necessary libraries
import Adafruit_PCA9685
pwm = Adafruit_PCA9685.PCA9685()


# steer control - R (right) L (left)
# throttle control - R (reverse) F (forward)

# frequency determined with oscilloscope. Called outside of steering/throttle functions to eliminate freq based bugs
pwm.set_pwm_freq(70)

# Steering and Throttle Trim
# + for Right turn or Forward
# Given in ms
steerTrim = 0
throttleTrim = 0

currentSpeed = 5
direction = True

# helper function to easily give steering commands


def stop():
    if direction:
        F_stop()
    else:
        R_stop()


def idleSpeed():
    throttle("F", 0)
    throttle("R", 0)


def changeSpeed(more):
    global currentSpeed
    if more:
        currentSpeed += 2
    else:
        currentSpeed -= 2
    currentSpeed = max(min(currentSpeed, 100), 5)


def throttleHelper(Dir):
    global direction
    direction = Dir
    throttle(Dir, currentSpeed)


def steer(Dir, Deg):

    # convert desired turn angle to required pulse width offset
    # relationship determined from laser diode angle testing
    pulse = Deg/79.301

    # add (right turn) or subtract (left turn) the pulse width offset from middle 1.5 ms
    if Dir == "R":
        pulse = 1.5 + pulse + steerTrim
    else:
        pulse = 1.5 - pulse + steerTrim

    # convert pulse width value to 12 bit number expected by PWM9685 library functions
    # relationship determined experimentally with oscilloscope testing
    # floor and int functions used because PWM9685 library functions cannot be passed a float
    py_pulse = int(math.floor(pulse/.0034)) + steerTrim

    # PWM9685 library function to give the module a command
    pwm.set_pwm(1, 0, py_pulse)


# helper function to easily give throttle commands
def throttle(Dir, Percent):

    # converts % throttle input to pulse width offset max of .5
    pulse = Percent/200

    # add (reverse) or subtract (forward) the pulse width offset from middle 1.5 ms
    if Dir == "R":
        pulse = 1.5 + pulse - throttleTrim
    else:
        pulse = 1.5 - pulse - throttleTrim

    # see steer() comments
    py_pulse = int(math.floor(pulse/.0034))
    pwm.set_pwm(12, 0, py_pulse)


# function to simulate full throttle and idle to release ESC throttle safety
# should be called prior to throttle operations
def engage():
    throttle("F", 0)
    time.sleep(2)
    throttle("F", 100)
    time.sleep(.25)
    throttle("F", 0)
    time.sleep(.25)


# function to simulate input required to cause ESC braking when travelling forward
def F_stop():
    throttle("R", 100)
    time.sleep(.2)
    throttle("R", 0)
    time.sleep(.2)

# function to simulate input required to cause ESC braking when travelling in reverse


def R_stop():
    throttle("F", 100)
    time.sleep(.2)
    throttle("F", 0)
    time.sleep(.2)

# parameters
# ------------------------------------------------------------------------------------------------------------------------


delay = 1
med_delay = 3
long_delay = 5

# test area
# -------------------------------------------------------------------------------------------------------------------------
