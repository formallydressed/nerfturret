#!/usr/bin/env python

import cwiid
import time
import wiringpi2
import wiringpi2_helper as wp
import wii_helper as wh

def main():
    wp.wiringPiSetup()
    wp.mcp23s08Setup(75,0,0)
    x_motor=wp.StepperMotor(75,76,77,78,f="x_motor.txt")
    y_motor=wp.StepperMotor(79,80,81,82,f="y_motor.txt")
    wm=wh.WiiMote()
    wm.led_set(1,1)
    while not (wm.button_plus() and wm.button_minus()):
        if wm.button_up():
            if y_motor.position<256:
                y_motor.forward()
        if wm.button_down():
            if y_motor.position>0:
                y_motor.backward()
        if wm.button_right():
            if x_motor.position<128:
                x_motor.forward()
        if wm.button_left():
            if x_motor.position>0:
                x_motor.backward()
    with open("x_motor", "w") as pos_file:
        pos_file.write(str(x_motor.position))
    with open("y_motor", "w") as pos_file:
        pos_file.write(str(y_motor.position))
    wm.rumble(1)
    print "Closing connection..."
    wm.led_set()
    

if __name__=="__main__":
    main()
