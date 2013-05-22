#!/usr/bin/env python

import cwiid
import time
import wiringpi2 as wp
import wiringpi2_helper as wph
import wii_helper as wh

wp.wiringPiSetup()
wp.mcp23s08Setup(75,1,0)
wp.mcp23s08Setup(120,0,0)

x_motor=wph.StepperMotor(76,78,75,77,f="x_motor.txt")
y_motor=wph.StepperMotor(80,82,79,81,f="y_motor.txt")
power_led=wph.Led(5)
wp.pinMode(6,0)
trigger=wph.Led(120)
flywheel=wph.Led(121)
laser=wph.Led(122)
wiiconnect=wph.Led(126)
wiinotconnect=wph.Led(127)
wp.pinMode(1,0)

trigger.off()
flywheel.off()
wiiconnect.off()
wiinotconnect.off()

def fire():
    if flywheel.state:        
        trigger.on()
        time.sleep(5)
        trigger.off()        

def control():
    wm=wh.WiiMote()
    wiinotconnect.off()
    wiiconnect.on()
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
        if wm.button_B():
            if flywheel.state:
                flywheel.off()
                wm.led_set(3,0)
                wm.led_set(4,0)
            else:
                flywheel.on()
                wm.led_set(3,1)
                time.sleep(2)
                wm.led_set(4,1)
            time.sleep(0.2)
        if wm.button_A():
            if laser.state:
                laser.off()
                wm.led_set(2,0)
            else:
                laser.on()
                wm.led_set(2,1)
            time.sleep(0.2)
        if wm.button_two():
            wm.led_set(4,0)
            fire()
            wm.led_set(4,1)
    with open("x_motor.txt", "w") as pos_file:
        pos_file.write(str(x_motor.position))
    with open("y_motor.txt", "w") as pos_file:
        pos_file.write(str(y_motor.position))
    wm.rumble(1)
    print "Closing connection..."
    wm.led_set()
    wiiconnect.off()
    wiinotconnect.on()

def main():
    power_led.on()
    try:
        while True:
            if (wp.digitalRead(1)==1):
                wiinotconnect.on()
                if (wp.digitalRead(6)==1):
                    try:
                        control()
                    except RuntimeError:
                        print "Remote not connected. Try again."
    except KeyboardInterrupt:
        flywheel.off()
        laser.off() 
        wiiconnect.off()
        wiinotconnect.on()
        time.sleep(1)
        wiinotconnect.off()
        power_led.off()
        time.sleep(4)
        trigger.off()
        exit(1)
    
if __name__=="__main__":
    main()
