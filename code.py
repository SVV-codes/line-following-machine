# line-following-machine

import RPi.GPIO as gpio

gpio.setmode(gpio.BOARD)

gpio.setwarnings(False)

gpio.setup(13,gpio.OUT)
gpio.setup(15,gpio.OUT)


leftSensor = 7
rightSensor = 10
gpio.setup(leftSensor,gpio.IN)
gpio.setup(rightSensor,gpio.IN)

def leftOn():
    gpio.output(15,1)

def leftOff():
    gpio.output(15,0)
    
    
def rightOn():
    gpio.output(13,1)


def rightOff():
    gpio.output(13,0)


def stopAll():
    gpio.output(13,0)
    gpio.output(15,0)



stopAll()   
while True:
    
    if gpio.input(leftSensor)==0 and gpio.input(rightSensor) == 0:  
        leftOff()
        rightOff()
        
    if gpio.input(leftSensor)==1 and gpio.input(rightSensor)==1:
        leftOn()
        rightOn()
        
    if gpio.input(leftSensor)==1 and gpio.input(rightSensor)==0:
        leftOn()
        rightOff()
        
    if gpio.input(leftSensor)==0 and gpio.input(rightSensor)==1:
        leftOff()
        rightOn() 
        
gpio.cleanup()
        
