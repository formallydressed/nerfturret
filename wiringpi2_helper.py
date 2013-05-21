#!/usr/bin/env python

import wiringpi2 as wp
import time

wp.wiringPiSetup()

class StepperMotor():
  def __init___(self, p1,p2,p3,p4,f=False, pos=False, delay=2):
    self.p1=p1
    self.p2=p2
    self.p3=p3
    self.p4=p4
    self.f=f
    self.pos=pos
    self.delay=delay/1000.0
    wp.pinMode(self.p1, 1)
    wp.pinMode(self.p2, 1)
    wp.pinMode(self.p3, 1)
    wp.pinMode(self.p4, 1)
    self.position=0
    if self.f:
      with open(self.f, "r") as pos_file:
        self.position=int(pos_file.read())
    if self.pos:
      self.position=self.pos
    
  def forward(self, steps=1, delay=self.delay):
    for i in range(0, steps):
      setStep(1, 0, 1, 0)
      time.sleep(delay)
      setStep(0, 1, 1, 0)
      time.sleep(delay)
      setStep(0, 1, 0, 1)
      time.sleep(delay)
      setStep(1, 0, 0, 1)
      time.sleep(delay)
      setStep(0, 0, 0, 0)
      self.position+=1

  def backwards(self, steps=1, delay=self.delay):
    for i in range(0, steps):
      setStep(1, 0, 0, 1)
      time.sleep(delay)
      setStep(0, 1, 0, 1)
      time.sleep(delay)
      setStep(0, 1, 1, 0)
      time.sleep(delay)
      setStep(1, 0, 1, 0)
      time.sleep(delay)
      setStep(0, 0, 0, 0)
      self.position-=1
  
  def setStep(self,w1, w2, w3, w4):
    wp.digitalWrite(self.p1, w1)
    wp.digitalWrite(self.p2, w2)
    wp.digitalWrite(self.p3, w3)
    wp.digitalWrite(self.p4, w4)

class led():
  def __init__(self,p):
    self.p=p
    wp.pinMode(self.p,1)

  def on(self):
    wp.digitalWrite(self.p,1)

  def off(self):
    wp.digitalWrite(self.p,0)
