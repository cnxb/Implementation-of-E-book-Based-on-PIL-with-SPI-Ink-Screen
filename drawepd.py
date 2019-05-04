import epd2in13
import time
import Image
import ImageDraw
import ImageFont
import os

def fulldraw(draw_image):
    epd = epd2in13.EPD()
    epd.init(epd.lut_full_update)
    epd.clear_frame_memory(0xFF)
    epd.set_frame_memory(draw_image , 0, 0)
    epd.display_frame()

    epd.delay_ms(2000)




def partdraw(draw_image):
    epd = epd2in13.EPD()
    epd.init(epd.lut_partial_update)
    epd.clear_frame_memory(0xFF)
    epd.set_frame_memory(draw_image , 0, 0)
    epd.display_frame()

    epd.delay_ms(2000)
