from adafruit_circuitplayground.express import cpx
from adafruit_circuitplayground.express import time
import random
cpx.pixels.brightness = 0.015
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (150, 255, 0)
OFF = (0, 0, 0)
zwischenspeicher = WHITE
zielfarbe = WHITE
rand = 1
wincounter = 0

def Loading():
    for i in range(0, 10):          # loading animation white
        cpx.pixels[i] = WHITE
        time.sleep((random.randint(0, 49)+i)/100)
    time.sleep(random.randint(5, 24)/10)
    for i in range(0, 10):          # done loading animation
        cpx.pixels[i] = OFF
        time.sleep(0.03)
    time.sleep(random.randint(0, 4)/10)

def Setup():
    Randomize()
    time.sleep(0.2)
    zwischenspeicher = cpx.pixels[0]
    zielfarbe = cpx.pixels[9]

def Randomize():    # colors all the pixels
    for i in range(0, 10):
        rand = random.randint(1, 4)
        if(rand == 1):
            cpx.pixels[i] = RED
        elif(rand == 2):
            cpx.pixels[i] = GREEN
        elif(rand == 3):
            cpx.pixels[i] = BLUE
        elif(rand == 4):
            cpx.pixels[i] = YELLOW
        time.sleep(0.1)
    time.sleep(0.5)

def Recolor():
    if(zwischenspeicher == RED):
        cpx.pixels[0] = GREEN
    elif(zwischenspeicher == GREEN):
        cpx.pixels[0] = BLUE
    elif(zwischenspeicher == BLUE):
        cpx.pixels[0] = YELLOW
    elif(zwischenspeicher == YELLOW):
        cpx.pixels[0] = RED

def Weiter():       # Methode Weiter
    zwischenspeicher = cpx.pixels[0]
    for i in range(0, 8):
        cpx.pixels[i] = cpx.pixels[i+1]
    cpx.pixels[8] = zwischenspeicher
    zwischenspeicher = cpx.pixels[0]

Loading()
Setup()
zwischenspeicher = cpx.pixels[0]
zielfarbe = cpx.pixels[9]
if cpx.switch:
    cpx.play_file("tryme.wav")

while True:
    cpx.pixels[9] = (0, 0, 0)
    zwischenspeicher = cpx.pixels[0]
    Recolor()
    time.sleep(0.12)
    cpx.pixels[9] = zielfarbe
    cpx.pixels[0] = zwischenspeicher

    if cpx.button_a:
        Recolor()
        Weiter()
    if cpx.button_b:
        Weiter()
    time.sleep(0.7)

    for i in range(0, 9):
        if(cpx.pixels[i] == zielfarbe):
            wincounter = wincounter+1
    if(wincounter == 9):
        for i in range(0, 4):
            cpx.play_tone(225, 0.5)
            cpx.play_tone(275, 0.5)
            cpx.play_tone(250, 0.5)
            cpx.play_tone(300, 1)
        cpx.play_tone(300, 0.1)
        cpx.play_tone(250, 0.1)
        cpx.play_tone(275, 0.1)
        cpx.play_tone(225, 0.1)
        time.sleep(0.3)
        for i in range(0, 10):
            cpx.pixels[i] = OFF
        time.sleep(0.5)
        Loading()
        Setup()
        if cpx.switch:
            cpx.play_file("ashwga.wav")
    wincounter = 0
