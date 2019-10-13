from adafruit_circuitplayground.express import cpx
import random
import time
cpx.pixels.brightness = 0.015
counter = 7
RED = (255, 0, 0)
GREEN = (0, 255, 0)
OFF = (0, 0, 0)

def playyes():
    counter = random.randint(1, 8)
    for i in range(1, 8):
        if counter == i:
            cpx.play_file("yes-"+str(i)+".wav")

def playno():
    counter = random.randint(1, 8)
    for i in range(1, 8):
        if counter == i:
            cpx.play_file("no-"+str(i)+".wav")

def flashled(color):
    for i in range(0, 10):
        cpx.pixels[i] = color

while True:
    flashled(OFF)
    if cpx.button_a:
        flashled(GREEN)
        playyes()
        time.sleep(1.5)
    elif cpx.button_b:
        flashled(RED)
        playno()
        time.sleep(1.5)
