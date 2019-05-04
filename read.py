# start

# -*- coding:utf-8 -*-


import epd2in13
import time
import Image
import ImageDraw
import ImageFont
import os
import drawepd
import codecs
import os
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)

image = Image.new('1', (epd2in13.EPD_WIDTH, epd2in13.EPD_HEIGHT), 255)
font = ImageFont.truetype(r'/home/pi/Documents/MSYH.TTC', 12)
draw = ImageDraw.Draw(image)
drawepd.partdraw(image)

x = 8
y = 10
f = codecs.open("/home/pi/now/books/book.txt", "r", "utf-8")
content = f.read()
print(type(content))


def toPage(k):
    line_x = 10
    line_y = 10
    temp = ""
    for j in range(y * k, y * k + y):
        temp = ""
        for i in range(x * j, x * j + x):
            temp = temp + content[i]
        draw.text((line_x, line_y), temp, font=font, fill=0)
        line_y += 20
    drawepd.partdraw(image)


z = 0

while True:
    '''
    if GPIO.input(20) == 1:
        while True:
            if GPIO.input(20) == 0:
                z = z + 1
                toPage(z)
                break
    if GPIO.input(21) == 1:
        while True:
            if GPIO.input(21) == 0:
                z = z - 1
                toPage(z)
                break
    '''
    z = z + 1
    toPage(z)
    image = Image.new('1', (epd2in13.EPD_WIDTH, epd2in13.EPD_HEIGHT), 255)
    font = ImageFont.truetype(r'/home/pi/Documents/MSYH.TTC', 12)
    draw = ImageDraw.Draw(image)
    time.sleep(1)

