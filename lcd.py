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
    displayText("o__0", BLACK, display.width // 2, display.height // 2)
    time.sleep(0.5)
    clearDisplay()
    
    displayText(":)", BLACK, display.width // 2, display.height // 2)  
    time.sleep(0.5)
    clearDisplay()

def clearDisplay():
    while (len(splash) > 1):
        splash.pop()

def displayDoge():
    odb = displayio.OnDiskBitmap('/doge.bmp')
    face = displayio.TileGrid(odb, pixel_shader=odb.pixel_shader)
    splash.append(face)
    time.sleep(0.5)
    clearDisplay()

# Display 
# "Hello my"
# "Name is"      ---->    "DIVY"
def displayIntro():
    displayText("Hi, my", BLACK, display.width // 2, display.height // 3, FONT_SCALE_LARGE)
    displayText("name is", BLACK, display.width // 2, 2 * display.height // 3, FONT_SCALE_LARGE)
    time.sleep(1)
    clearDisplay()
    displayText("DIVY", BLACK, display.width // 2, display.height // 2, FONT_SCALE_EXTRA_LARGE)
    time.sleep(1)
    clearDisplay()

def displayAsciiFace():
    pass


def displayColorFace():
    palette = displayio.Palette(1)
    palette[0] = WHITE
    palette[1] = BLACK
    left_eye = vectorio.Circle(pixel_shader=palette, radius = 20, x = display.width // 3, y = display.height // 3)
    left_pupil = vectorio.Circle(pixel_shader=palette, radius = 10, x = display.width // 3, y = display.height // 3, color_index=1)
    # nose = vectorio.Polygon(pixel_shader=palette, points=[])
    right_eye = vectorio.Circle(pixel_shader=palette, radius = 20, x = 2 * display.width // 3, y = display.height // 3)
    right_pupil = vectorio.Circle(pixel_shader=palette, radius = 10, x = 2 * display.width // 3, y = display.height // 3, color_index=1)
    mouth = vectorio.Rectangle(pixel_shader=palette, width = display.width // 2, height = display.height // 7, x = display.width // 4, y = display.height // 4 * 3 )
    splash.append(left_eye)
    splash.append(left_pupil)
    splash.append(right_eye)
    splash.append(right_pupil)
    splash.append(mouth)
    time.sleep(1)
    


def displayRainbowStream():
    color_palette = displayio.Palette(7)
    color_list =  [RED, ORANGE, YELLOW, GREEN, BLUE, INDIGO, VIOLET]
    for i in range(len(color_list)):
        color_palette[i] = color_list[i]
    
    color_bitmap2 = displayio.Bitmap((display.width // 7) * 7, display.height, 1)
    tile_grid = displayio.TileGrid(bitmap = color_bitmap2, pixel_shader = color_palette, tile_width=display.width // 7)
    
    
    splash.append(tile_grid)
    time.sleep(5)
    clearDisplay()

    # divide screen into 7 containers

    # shift container values over to the right


def displayRainbowStreamManual():
    color_palette = displayio.Palette(7)
    color_list =  [RED, ORANGE, YELLOW, GREEN, BLUE, INDIGO, VIOLET]
    
    global setup_rainbow
    global rainbow
    if setup_rainbow == False:
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
        setup_rainbow = True

    for offset in range(7): # colors_list.len
        for element in range(len(rainbow)):
            rainbow[element].fill((element + offset) % 7)
        time.sleep(1/60 * 2)
        

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

color_bitmap = displayio.Bitmap(display.width, display.height, 1)

color_pal = displayio.Palette(1)
color_pal[0] = BLACK

bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_pal, x=0, y=0)
splash.append(bg_sprite)

setup_rainbow = False

'''
Superloop
'''
while True:
    print("Code starting")
    
    #testDisplay()

    # displayIntro()

    #displayDoge()

    # displayRainbowStreamManual()

    displayColorFace()