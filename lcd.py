# https://github.com/adafruit/Adafruit_CircuitPython_ST7789/blob/main/examples/st7789_240x135_simpletest_Pimoroni_Pico_Display_Pack.py
# https://docs.circuitpython.org/projects/st7789/en/latest/examples.html#x135
# https://docs.circuitpython.org/projects/st7789/en/latest/
# https://learn.adafruit.com/making-a-pyportal-user-interface-displayio/groups

import board
import displayio

import busio

import digitalio
import time

import terminalio

from adafruit_st7789 import ST7789
from adafruit_display_text import label

# First set some parameters used for shapes and text
BORDER = 20
FONTSCALE = 2
BACKGROUND_COLOR = 0x00FF00  # Bright Green
FOREGROUND_COLOR = 0xAA0088  # Purple
TEXT_COLOR = 0xFFFF00



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

display = ST7789(
    display_bus, rotation=270, width=240, height=135, rowstart=40, colstart=53
)


# Make the display context
splash = displayio.Group()
display.show(splash)

color_bitmap = displayio.Bitmap(display.width, display.height, 1)
color_palette = displayio.Palette(1)
color_palette[0] = BACKGROUND_COLOR

bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
splash.append(bg_sprite)

# Draw a smaller inner rectangle
inner_bitmap = displayio.Bitmap(
    display.width - BORDER * 2, display.height - BORDER * 2, 1
)
inner_palette = displayio.Palette(1)
inner_palette[0] = FOREGROUND_COLOR
inner_sprite = displayio.TileGrid(
    inner_bitmap, pixel_shader=inner_palette, x=BORDER, y=BORDER
)
splash.append(inner_sprite)




'''


# Make the display context
splash = displayio.Group()
display.show(splash)

color_bitmap = displayio.Bitmap(135, 240, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0x00FF00

bg_sprite = displayio.TileGrid(color_bitmap,
                               pixel_shader=color_palette, x=0, y=0)
splash.append(bg_sprite)

# Draw a smaller inner rectangle
inner_bitmap = displayio.Bitmap(133, 238, 1)
inner_palette = displayio.Palette(1)
inner_palette[0] = 0x0000FF
inner_sprite = displayio.TileGrid(inner_bitmap,
                                  pixel_shader=inner_palette, x=1, y=1)
splash.append(inner_sprite)

# Draw a label
text_group1 = displayio.Group(max_size=10, scale=2, x=20, y=40)
text1 = "RPi Pico"
text_area1 = label.Label(terminalio.FONT, text=text1, color=0xFF0000)
text_group1.append(text_area1)  # Subgroup for text scaling
# Draw a label
text_group2 = displayio.Group(max_size=10, scale=1, x=20, y=60)
text2 = "CircuitPython"
text_area2 = label.Label(terminalio.FONT, text=text2, color=0xFFFFFF)
text_group2.append(text_area2)  # Subgroup for text scaling

# Draw a label
text_group3 = displayio.Group(max_size=10, scale=1, x=20, y=100)
text3 = adafruit_st7789.__name__
text_area3 = label.Label(terminalio.FONT, text=text3, color=0x0000000)
text_group3.append(text_area3)  # Subgroup for text scaling
# Draw a label
text_group4 = displayio.Group(max_size=10, scale=2, x=20, y=120)
text4 = adafruit_st7789.__version__
text_area4 = label.Label(terminalio.FONT, text=text4, color=0x000000)
text_group4.append(text_area4)  # Subgroup for text scaling

splash.append(text_group1)
splash.append(text_group2)
splash.append(text_group3)
splash.append(text_group4)


'''


# print different lines of text
text_list = [":)", "hello", "bye"]

while True:
    

    
    # Output refreshing text    
    text = "0 _ 0"
    text_area = label.Label(terminalio.FONT, text=text, color=TEXT_COLOR)
    text_width = text_area.bounding_box[2] * FONTSCALE
    text_group = displayio.Group(
        scale=FONTSCALE,
        x=display.width // 2 - text_width // 2,
        y=display.height // 2,
    )
    text_group.append(text_area)  # Subgroup for text scaling
    splash.append(text_group)
    time.sleep(0.5)
    splash.remove(text_group)
    
    text = ":)"
    text_area = label.Label(terminalio.FONT, text=text, color=TEXT_COLOR)
    text_width = text_area.bounding_box[2] * FONTSCALE
    text_group = displayio.Group(
        scale=FONTSCALE,
        x=display.width // 2 - text_width // 2,
        y=display.height // 2,
    )
    text_group.append(text_area)  # Subgroup for text scaling
    splash.append(text_group)
    time.sleep(0.5)
    splash.pop()
    