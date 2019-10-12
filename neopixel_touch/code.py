from adafruit_circuitplayground.express import cpx
import time
cpx.pixels.brightness = 0.015

while True:
    if cpx.button_a and cpx.button_b:
        cpx.pixels.brightness = 1
        time.sleep(0.3)
    elif cpx.button_a:
        cpx.pixels.brightness = 0.015
    elif cpx.button_b:
        cpx.pixels.brightness = 0.115
    if cpx.touch_A1:
        cpx.pixels[5] = (255, 0, 0)
    if cpx.touch_A2:
        cpx.pixels[7] = (255, 0, 0)
    if cpx.touch_A3:
        cpx.pixels[9] = (255, 0, 0)
    if cpx.touch_A4:
        cpx.pixels[0] = (255, 0, 0)
    if cpx.touch_A5:
        cpx.pixels[2] = (255, 0, 0)
    if cpx.touch_A6:
        cpx.pixels[4] = (255, 0, 0)
    if cpx.touch_A7:
        cpx.pixels[0] = (0, 0, 0,)
        cpx.pixels[2] = (0, 0, 0,)
        cpx.pixels[4] = (0, 0, 0,)
        cpx.pixels[5] = (0, 0, 0,)
        cpx.pixels[7] = (0, 0, 0,)
        cpx.pixels[9] = (0, 0, 0,)
