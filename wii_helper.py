#!/usr/bin/env python

import cwiid
import time

class WiiMote():
    def __init__(self):
        print "Press buttons 1 + 2 on your Wii Remote"
        time.sleep(1)
        self.wm=cwiid.Wiimote()
        print "Wii Remote connected"
        print "Press the Plus and Minus buttons together to disconnect the Remote"
        wm.rpt_mode=cwiid.RPT_BTN
        self.led_state=0

    def button_up(self, only=False):
        if only: return (self.wm.state["buttons"]-cwiid.BTN_UP)==0
        else: return (self.wm.state["buttons"]&cwiid.BTN_UP)!=0

    def button_down(self, only=False):
        if only: return (self.wm.state["buttons"]-cwiid.BTN_DOWN)==0
        else: return (self.wm.state["buttons"]&cwiid.BTN_DOWN)!=0

    def button_right(self, only=False):
        if only: return (self.wm.state["buttons"]-cwiid.BTN_RIGHT)==0
        else: return (wm.state["buttons"]&cwiid.BTN_RIGHT)!=0

    def button_left(self, only=False):
        if only: return (self.wm.state["buttons"]-cwiid.BTN_LEFT)==0
        else: return (self.wm.state["buttons"]&cwiid.BTN_LEFT)!=0

    def button_plus(self, only=False):
        if only: return (self.wm.state["buttons"]-cwiid.BTN_PLUS)==0
        else: return (self.wm.state["buttons"]&cwiid.BTN_PLUS)!=0

    def button_minus(self, only=False):
        if only: return (self.wm.state["buttons"]-cwiid.BTN_MINUS)==0
        else: return (self.wm.state["buttons"]&cwiid.BTN_MINUS)!=0

    def button_two(self, only=False):
        if only: return (self.wm.state["buttons"]-cwiid.BTN_ONE)==0
        else: return (self.wm.state["buttons"]&cwiid.BTN_ONE)!=0

    def button_one(self, only=False):
        if only: return (self.wm.state["buttons"]-cwiid.BTN_TWO)==0
        else: return (self.wm.state["buttons"]&cwiid.BTN_TWO)!=0

    def button_A(self, only=False):
        if only: return (self.wm.state["buttons"]-cwiid.BTN_A)==0
        else: return (self.wm.state["buttons"]&cwiid.BTN_A)!=0

    def button_B(self, only=False):
        if only: return (self.wm.state["buttons"]-cwiid.BTN_B)==0
        else: return (self.wm.state["buttons"]&cwiid.BTN_B)!=0

    def button_home(self, only=False):
        if only: return (self.wm.state["buttons"]-cwiid.BTN_HOME)==0
        else: return (self.wm.state["buttons"]&cwiid.BTN_HOME)!=0

    def led_set(self, num=False, state=False):
        if num:
            if ((2**(num-1))&self.led_state)==0:
                if state:
                    self.led_state+=(2**(num-1))
                    self.wm.led=self.led_state
            else:
                if not state:
                    self.led_state-=(2**(num-1))
                    self.wm.led=self.led_state
                    
        else: self.wm.led=0

    def rumble(self, t):
        if t:
            self.wm.rumble=1
            time.sleep(t)
            self.wm.rumble=0
        
    
    
