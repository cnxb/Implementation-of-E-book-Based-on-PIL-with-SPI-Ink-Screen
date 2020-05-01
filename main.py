#!/usr/bin/python
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
GPIO.setup(22, GPIO.OUT)



bookslist=os.listdir("/home/pi/now/books")
image = Image.new('1', (epd2in13.EPD_WIDTH, epd2in13.EPD_HEIGHT), 255)    
font =ImageFont.truetype(r'/home/pi/Documents/MSYH.TTC', 12)
draw = ImageDraw.Draw(image)

book_x=10
book_y=10
select_S=0
number_S=0
while True:
    for i in bookslist:
        if number_S!=select_S:
            draw.text((book_x,book_y),str(numbers)+i, font = font, fill = 0)
        else:    
            while GPIO.input(22) == 1:
                time.sleep(0.1)
                if GPIO.input(22) == 0:
                    os.system("python3 read.py "+i)

        book_y+=10
        print(book_x,book_y)
        numbers+=1
    drawepd.partdraw(image)
    #判  断
    while GPIO.input(20) == 1:
        time.sleep(0.1)
        if GPIO.input(20) == 0:
            select_S = zselect_S + 1
            
    while GPIO.input(21) == 1:
        time.sleepz(0.1)
        if GPIO.input(21) == 0:
            select_S = select_S - 1