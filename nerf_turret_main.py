#!/usr/bin/env python

import cwiid
import time
import wiringpi2 as wp
import wiringpi2_helper as wph
import wii_helper as wh

wp.wiringPiSetup()
wp.mcp23s08Setup(75,0,0)
x_motor=wph.StepperMotor(76,78,75,77,f="x_motor.txt")
y_motor=wph.StepperMotor(80,82,79,81,f="y_motor.txt")
wp.pinMode(1,0)

def control():
    wm=wh.WiiMote()
    wm.led_set(1,1)
    while not (wm.button_plus() and wm.button_minus()):
        if wm.button_up():
            if y_motor.position<256:
                y_motor.forward()
        if wm.button_down():
            if y_motor.position>0:
                y_motor.backwards()
        if wm.button_right():
            if x_motor.position<128:
                x_motor.forward()
        if wm.button_left():
            if x_motor.position>0:
                x_motor.backwards()
        if wm.button_home():
            x_motor.specific(64)
            y_motor.specific(128)
    with open("x_motor.txt", "w") as pos_file:
        pos_file.write(str(x_motor.position))
    with open("y_motor.txt", "w") as pos_file:
        pos_file.write(str(y_motor.position))
    wm.rumble(1)
    print "Closing connection..."
    wm.led_set()

def main():
    while True:
        if (wp.digitalRead(1)==1):
            try:
                control()
            except RuntimeError:
                print "Remote not connected. Try again."
    
if __name__=="__main__":
    main()
