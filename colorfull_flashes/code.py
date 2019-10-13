
from adafruit_circuitplayground.express import cpx
import random
import time
bright = cpx.pixels.brightness
cpx.pixels.brightness = 0.115
speed = 0
rand = 0
red = 0
green = 0
blue = 0
zufzahl = 0
zufselect = 0
remember_reset = True

def Reset():
    global speed
    cpx.pixels.brightness = 0.115
    speed = 0

def Randcolor():
    global red, green, blue, zufselect
    zufselect = zufselect+1
    red = 0
    green = 0
    blue = 0
    if zufselect == 1:
        red = random.randint(0, 255)
    elif zufselect == 2:
        green = random.randint(0, 255)
    elif zufselect == 3:
        blue = random.randint(0, 255)
    elif zufselect == 4:
        red = random.randint(0, 255)
        green = random.randint(0, 255)
    elif zufselect == 5:
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
    elif zufselect == 6:
        blue = random.randint(0, 255)
        red = random.randint(0, 255)
    elif zufselect == 7:
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        zufselect = 0

while True:
    if cpx.switch:
        if remember_reset:
            Reset()
            remember_reset = False
        for i in range(0, 10):
            Randcolor()
            cpx.pixels[i] = (red, green, blue)
        time.sleep(speed)
        for i in range(0, random.randint(0, 9)):
            cpx.pixels[random.randint(0, 9)] = (0, 0, 0)
        time.sleep(speed)
        for i in range(0, 10):
            cpx.pixels[i] = (0, 0, 0)
        if cpx.button_a:
            if(speed < 0.5):
                speed = speed + 0.1
            else:
                speed = 0
                time.sleep(0.1)
        if cpx.button_b:
            if(bright < 0.5):
                bright = bright + 0.1
            else:
                bright = 0.015
                time.sleep(0.5)
            cpx.pixels.brightness = bright
    else:
        remember_reset = True
