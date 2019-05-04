#!/usr/bin/python
# -*- coding:utf-8 -*-



import epd2in13
import time
import Image
import ImageDraw
import ImageFont
import os
import drawepd



bookslist=os.listdir("/home/pi/now/books")
image = Image.new('1', (epd2in13.EPD_WIDTH, epd2in13.EPD_HEIGHT), 255)    
font =ImageFont.truetype(r'/home/pi/Documents/MSYH.TTC', 12)
draw = ImageDraw.Draw(image)

book_x=10
book_y=10
for i in bookslist:
    draw.text((book_x,book_y),i, font = font, fill = 0)
    book_y+=10
    print(book_x,book_y)
drawepd.fulldraw(image)

