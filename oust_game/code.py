from adafruit_circuitplayground.express import cpx
import random
import time

cpx.pixels.brightness = 0.05

COLOR_RED = (255, 0, 0)
COLOR_YELLOW = (255, 255, 0)
COLOR_GREEN = (0, 255, 0)
COLOR_NONE = (0, 0, 0)

def led(num, color):
    cpx.pixels[num] = color

def leds(begin, end, color):
    for i in range(begin, end):
        led(i, color)

def ledPattern(count, color, offset=0):
    for i in range(offset, 10, count):
        led(i, color)

def randomColor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def play():
    prevx = 0
    prevy = 0
    prevz = 0

    difx = 0
    dify = 0
    difz = 0

    maxdif = 15

    leds(0, 10, COLOR_RED)
    time.sleep(1)
    leds(0, 10, COLOR_YELLOW)
    time.sleep(1)
    leds(0, 10, COLOR_GREEN)
    time.sleep(1)
    leds(0, 10, randomColor())

    while difx < maxdif and dify < maxdif and difz < maxdif:
        x = cpx.acceleration[0]
        y = cpx.acceleration[1]
        z = cpx.acceleration[2]

        difx = abs(x - prevx)
        dify = abs(y - prevy)
        difz = abs(z - prevz)

        prevx = x
        prevy = y
        prevz = z

        print((difx, dify, difz))

        time.sleep(0.1)

        prevx = x
        prevy = y
        prevz = z

def main():
    while True:
        if cpx.button_a and cpx.button_b:
            time.sleep(2)
            if cpx.button_a and cpx.button_b:
                play()
                leds(0, 10, COLOR_NONE)

while True:
    main()
