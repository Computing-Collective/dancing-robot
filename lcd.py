# https://github.com/adafruit/Adafruit_CircuitPython_ST7789/blob/main/examples/st7789_240x135_simpletest_Pimoroni_Pico_Display_Pack.py
# https://docs.circuitpython.org/projects/st7789/en/latest/examples.html#x135
# https://docs.circuitpython.org/projects/st7789/en/latest/
# https://learn.adafruit.com/making-a-pyportal-user-interface-displayio/groups
# https://github.com/adafruit/Adafruit_CircuitPython_ST7789/blob/main/examples/st7789_240x135_simpletest_Pimoroni_Pico_Display_Pack.py

import board
import displayio # https://docs.circuitpython.org/en/latest/shared-bindings/displayio/index.html

import busio

import digitalio
import time

import terminalio # https://docs.circuitpython.org/en/latest/shared-bindings/terminalio/index.html

from adafruit_st7789 import ST7789 # https://docs.circuitpython.org/projects/st7789/en/latest/
from adafruit_display_text import label # https://docs.circuitpython.org/projects/display_text/en/latest/api.html#adafruit_display_text.bitmap_label.Label
import vectorio

'''

Constants

'''

BLACK = 0x000000
WHITE = 0xFFFFFF
RED = 0xFF0000
GREEN = 0x00FF00
BLUE = 0x0000FF
YELLOW = 0xFFFF00
CYAN = 0x00FFFF
MAGENTA = 0xFF00FF
ORANGE = 0xFFA500
INDIGO = 0x4B0082
VIOLET = 0x8F00FF

BORDER = 20
BACKGROUND_COLOR = 0x00FF00  # Bright Green 
FOREGROUND_COLOR = 0xAA0088  # Purple
TEXT_COLOR = GREEN

FONT_SCALE_SMALL = 1
FONT_SCALE_MEDIUM = 2
FONT_SCALE_LARGE = 3
FONT_SCALE_EXTRA_LARGE = 8 # Full screen height

# Example temp function for displaying basics
def testDisplay():
    clearDisplay()
    displayText("o__0", BLACK, display.width // 2, display.height // 2)
    time.sleep(0.5)

    clearDisplay()
    displayText(":)", BLACK, display.width // 2, display.height // 2)  
    time.sleep(0.5)

def clearDisplay():
    while (len(splash) > 1):
        splash.pop()

def displayDoge():
    clearDisplay()
    odb = displayio.OnDiskBitmap('/doge.bmp')
    face = displayio.TileGrid(odb, pixel_shader=odb.pixel_shader)
    splash.append(face)
    time.sleep(0.5)

# Display 
# "Hello my"
# "Name is"      ---->    "DIVY"
def displayIntro():

    clearDisplay()
    displayText("Hi, my", BLACK, display.width // 2, display.height // 3, FONT_SCALE_LARGE)
    displayText("name is", BLACK, display.width // 2, 2 * display.height // 3, FONT_SCALE_LARGE)
    time.sleep(1)
    
    clearDisplay()
    displayText("DIVY", BLACK, display.width // 2, display.height // 2, FONT_SCALE_EXTRA_LARGE)
    time.sleep(1)

def displayAsciiFace():
    clearDisplay()
    displayText("[||] [||]", BLACK, display.width // 2, display.height // 3, FONT_SCALE_LARGE)
    displayText("____", BLACK, display.width // 2, 2 * display.height // 3, FONT_SCALE_LARGE)
    time.sleep(0.5)
    
    clearDisplay()
    displayText("[X] [X]", BLACK, display.width // 2, display.height // 3, FONT_SCALE_LARGE)
    displayText("O", BLACK, display.width // 2, 2 * display.height // 3, FONT_SCALE_LARGE)
    time.sleep(0.5)

def displayColorFace():
    clearDisplay()

    palette = displayio.Palette(3)
    palette[0] = WHITE
    palette[1] = BLACK
    palette[2] = RED
    
    left_eye = vectorio.Circle(pixel_shader=palette, radius = 20, x = display.width // 3, y = display.height // 3)
    left_pupil = vectorio.Circle(pixel_shader=palette, radius = 10, x = display.width // 3, y = display.height // 3, color_index=1)

    # points for a triangle (nose)
    points = [
        (120, 65), # top middle
        (110, 75), # left bottom
        (130, 75) # left right
        ]
    nose = vectorio.Polygon(pixel_shader=palette, points=points, x = 0, y = 0, color_index = 2)
    
    right_eye = vectorio.Circle(pixel_shader=palette, radius = 20, x = 2 * display.width // 3, y = display.height // 3)
    right_pupil = vectorio.Circle(pixel_shader=palette, radius = 10, x = 2 * display.width // 3, y = display.height // 3, color_index=1)
    mouth = vectorio.Rectangle(pixel_shader=palette, width = display.width // 2, height = display.height // 7, x = display.width // 4, y = display.height // 4 * 3 )

    splash.append(left_eye)
    splash.append(left_pupil)
    splash.append(right_eye)
    splash.append(right_pupil)
    splash.append(mouth)
    splash.append(nose)
    
    time.sleep(1)
    
def displayArrows():
    clearDisplay()

    palette = displayio.Palette(3)
    palette[0] = CYAN
    palette[1] = MAGENTA
    palette[2] = ORANGE

    # points for a triangle (nose)
    points = [
        (140, 30), # top 
        (220, (105+30)//2), # right
        (140, 105) # bottom
        ]
    right_triangle = vectorio.Polygon(pixel_shader=palette, points=points, x = 0, y = 0, color_index = 2)
    right_rect = vectorio.Rectangle(pixel_shader=palette, width = display.width // 2, height = display.height // 4, x = 20, y = (display.height // 2) - (display.height // 4) // 2 )
    splash.append(right_rect)
    splash.append(right_triangle)
    time.sleep(0.7)

    clearDisplay()
    # points for a triangle (nose)
    points = [
        (100, 30), # top 
        (20, (105+30)//2), # right
        (100, 105) # bottom
        ]
    left_triangle = vectorio.Polygon(pixel_shader=palette, points=points, x = 0, y = 0, color_index = 2)
    left_rect = vectorio.Rectangle(pixel_shader=palette, width = display.width // 2, height = display.height // 4, x = 100, y = (display.height // 2) - (display.height // 4) // 2 )
    splash.append(left_rect)
    splash.append(left_triangle)
    time.sleep(0.7)

def displayRainbowStreamManual():
    color_palette = displayio.Palette(7)
    color_list =  [RED, ORANGE, YELLOW, GREEN, BLUE, INDIGO, VIOLET]
    
    rainbow = [] # list of displayio.Bitmap
    for i in range(len(color_list)):
        color_palette[i] = color_list[i]

    for i in range(7): # colors_list.len
        bmp_name = "temp_bmp_" + str(i)
        sprite_name = "temp_sprite_" + str(i)
        bmp_name = displayio.Bitmap(display.width // 7, display.height, 7)
        bmp_name.fill(i)
        sprite_name = displayio.TileGrid(bmp_name, pixel_shader=color_palette, tile_width=display.width // 7, tile_height=display.height, x=i*(display.width // 7), y=0)
        rainbow.append(bmp_name)
        splash.append(sprite_name)

    for i in range(3):
        for offset in range(7): # colors_list.len
            for element in range(len(rainbow)):
                rainbow[element].fill((element + offset) % 7)
            time.sleep(0.05)

    clearDisplay()
        

    # # make the rainbow shift over
    # for shift in range(100):
    #     # make 7 coloured rectangles and add to group with x offset
    #     rainbow = displayio.Group(scale=1, x=0, y=0)
    #     for i in range(len(color_list)):
    #         temp_bmp = displayio.Bitmap(display.width // 7, display.height, 7)
    #         # Start filling in the colours left to right from a shifted index in color_list
    #         temp_bmp.fill((i + shift) % 7)
    #         temp_sprite = displayio.TileGrid(temp_bmp, pixel_shader=color_palette, tile_width=display.width // 7, tile_height=display.height, x=i*(display.width // 7), y=0)
    #         rainbow.append(temp_sprite)
    #     splash.append(rainbow)
    #     time.sleep(0.00001)
    #     # how does this work???
    #     splash.remove(rainbow)

def displayColorBlocks():
    # Draw a smaller inner rectangle
    inner_bitmap = displayio.Bitmap(
        display.width - BORDER * 2, display.height - BORDER * 2, 1
    )
    inner_palette = displayio.Palette(1)
    inner_palette[0] = RED
    inner_sprite = displayio.TileGrid(
        inner_bitmap, pixel_shader=inner_palette, x=BORDER, y=BORDER
    )
    splash.append(inner_sprite)
    
'''
@brief: display a coloured string of text at an (x,y) location on the display
@param str: the string to print
@param c: the color of the text (ex: 0xFFFFFF)
@param x: x location for the text to be displayed. 0 <= x <= 135
@param y: y location for the text to be displayed. 0 <= y <= 240
'''
def displayText(text: str, c, x: int, y: int, font_scale: int):
    text_area = label.Label(terminalio.FONT, text=text, color=c)
    text_width = text_area.bounding_box[2] * font_scale
    text_group = displayio.Group(
        scale=font_scale,
        x= x - text_width // 2,
        y= y,
    )
    text_group.append(text_area)
    splash.append(text_group)


'''
Initialization of SPI for display (global)
'''
# Release any resources currently in use for the displays
displayio.release_displays()

# set up GPIO
tft_dc = board.GP8
tft_cs = board.GP9
spi_clk = board.GP10
spi_mosi = board.GP11
tft_res = board.GP12

spi = busio.SPI(spi_clk, MOSI=spi_mosi)

#spi = board.SPI() does not work
while not spi.try_lock():
    pass
spi.configure(baudrate=24000000) # Configure SPI for 24MHz
spi.unlock()

display_bus = displayio.FourWire(spi, command=tft_dc, chip_select=tft_cs, reset=tft_res)

# Create the display object
display = ST7789(
    display_bus, rotation=270, width=240, height=135, rowstart=40, colstart=53
)

'''
Initialization the background (global)
'''
# Make the display context
splash = displayio.Group()
display.show(splash)

color_bitmap = displayio.Bitmap(display.width, display.height, 2)

color_pal = displayio.Palette(2)
color_pal[0] = BLACK
color_pal[1] = WHITE

bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_pal, x=0, y=0)
splash.append(bg_sprite)


'''
Superloop
'''
while True:
    print("Code starting")
    
    displayIntro()

    displayDoge()

    displayArrows()

    displayRainbowStreamManual()
    
    color_bitmap.fill(0) # fill background black
    displayColorFace()

    color_bitmap.fill(1) # fill background white
    displayAsciiFace()