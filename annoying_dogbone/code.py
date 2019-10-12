# /bin/hacken GameJam 2019, f0wL

"""This example lights up the third NeoPixel while button A is being pressed, and lights up the
eighth NeoPixel while button B is being pressed."""

from adafruit_circuitplayground.express import cpx
import random
import time
import math

cpx.pixels.brightness = 0.1

while True:
        rnd = random.randrange(1,10,1)
        rnd1 = random.randrange(0,255,1)
        rnd2 = random.randrange(0,255,1)
        rnd3 = random.randrange(0,255,1)
        cpx.pixels[rnd] = (rnd1, rnd2, rnd3)

        if rnd < 5:
            if cpx.button_b:
                cpx.play_file("dog.wav")

        if rnd > 5:
            if cpx.button_a:
                cpx.play_file("dog.wav")
        cpx.pixels.fill((0,0,0))
