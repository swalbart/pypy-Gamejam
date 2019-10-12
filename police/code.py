from adafruit_circuitplayground.express import cpx
import time

cpx.pixels.brightness = 0.05

COLOR_RED = (255, 0, 0)
COLOR_BLUE = (0, 0, 255)
COLOR_NONE = (0, 0, 0)

def led(num, color):
    cpx.pixels[num] = color

def leds(begin, end, color):
    for i in range(begin, end):
        led(i, color)

def ledPattern(count, color, offset=0):
    for i in range(offset, 10, count):
        led(i, color)

def turnup(c, t=0.1):
    for i in range(0, 10, 1):
        led(i, c)
        time.sleep(t)

def turndown(c=(0, 0, 0), t=0.1):
    for i in range(9, 0, -1):
        led(i, c)
        time.sleep(t)

def roundabout(c, t=0.02):
    for i in range(0, 10, 1):
        led(i, c)
        time.sleep(t)
        led(i, COLOR_NONE)

def police(t=0.3):
    for i in range(10):
        leds(0, 5, COLOR_RED)
        leds(5, 10, COLOR_BLUE)
        time.sleep(t)
        leds(0, 5, COLOR_BLUE)
        leds(5, 10, COLOR_RED)
        time.sleep(t)

    for i in range(10):
        ledPattern(2, COLOR_RED, 0)
        ledPattern(2, COLOR_BLUE, 1)
        time.sleep(t/3)
        ledPattern(2, COLOR_RED, 1)
        ledPattern(2, COLOR_BLUE, 0)
        time.sleep(t/3)

    for i in range(10):
        turnup(COLOR_RED, t/10)
        turnup(COLOR_BLUE, t/10)

while True:
    police()
