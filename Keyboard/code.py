from adafruit_circuitplayground.express import cpx

cpx.pixels.brightness = 0.1

last_tone = 0

def play(tone):
    global last_tone
    if last_tone != tone or last_tone == 0:
        cpx.stop_tone()
        cpx.start_tone(tone)
        last_tone = tone

def stop_playing():
    global last_tone
    cpx.stop_tone()
    last_tone = 0

def resetLed():
    for i in range(10):
        cpx.pixels[i] = (0, 0, 0)

def setLed(num, color):
    for i in range(10):
        if i == num:
            cpx.pixels[i] = color
        else:
            cpx.pixels[i] = (0, 0, 0)

while True:
    if cpx.touch_A1:
        setLed(6, (255, 0, 0))
        play(262)
    elif cpx.touch_A2:
        setLed(7, 0x6A5ACD)
        play(294)
    elif cpx.touch_A3:
        setLed(8, 0xFFE4B5)
        play(330)
    elif cpx.touch_A4:
        setLed(0, 0x6495ED)
        play(349)
    elif cpx.touch_A5:
        setLed(1, 0x40E0D0)
        play(392)
    elif cpx.touch_A6:
        setLed(3, 0x3CB371)
        play(440)
    elif cpx.touch_A7:
        setLed(4, 0xB8860B)
        play(494)
    else:
        resetLed()
        stop_playing()
