import board
import displayio  # https://docs.circuitpython.org/en/latest/shared-bindings/displayio/index.html

import busio

import digitalio
import time

import terminalio  # https://docs.circuitpython.org/en/latest/shared-bindings/terminalio/index.html

from adafruit_st7789 import (
    ST7789,
)  # https://docs.circuitpython.org/projects/st7789/en/latest/
from adafruit_display_text import (
    label,
)  # https://docs.circuitpython.org/projects/display_text/en/latest/api.html#adafruit_display_text.bitmap_label.Label
import vectorio

from constants import *

"""

Constants

"""

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
FONT_SCALE_EXTRA_LARGE = 8  # Full screen height


class LCD:
    def __init__(self, display_bus):
        """
        Initialization of SPI for display (global)
        """

        # spi = board.SPI() does not work
        # Create the display object
        self.display = ST7789(
            display_bus, rotation=270, width=240, height=135, rowstart=40, colstart=53
        )

        """
        Initialization the background (global)
        """
        # Make the display context
        self.splash = displayio.Group()
        self.display.show(self.splash)

        self.color_bitmap = displayio.Bitmap(self.display.width, self.display.height, 2)

        color_pal = displayio.Palette(2)
        color_pal[0] = BLACK
        color_pal[1] = WHITE

        bg_sprite = displayio.TileGrid(
            self.color_bitmap, pixel_shader=color_pal, x=0, y=0
        )
        self.splash.append(bg_sprite)

        """
        Rainbow
        """
        self.rainbow = []  # list of displayio.Bitmap
        self.rainbow_counter = 0

        """
        Doge
        """
        odb = displayio.OnDiskBitmap("/doge.bmp")
        self.face = displayio.TileGrid(odb, pixel_shader=odb.pixel_shader)

    # Example temp function for displaying basics
    def testDisplay(self, ticks):  # works
        if ticks == 1:
            self.displayText(
                "o__0",
                WHITE,
                self.display.width // 2,
                self.display.height // 2,
                FONT_SCALE_MEDIUM,
            )

        # self.displayText(":)", BLACK, self.display.width // 2, self.display.height // 2, FONT_SCALE_MEDIUM)

    def clearDisplay(self):
        while len(self.splash) > 1:
            self.splash.pop()

    def displayDoge(self, ticks):
        if ticks == 1:
            self.clearDisplay()
            self.splash.append(self.face)

    def displayIntro(self, ticks):
        """
        Animation time is 2 seconds, but it can be stopped in the middle
        Display
        "Hello my"
        "Name is"      ---->    "DIVY"
        """
        if ticks == 1:
            print("displaying Intro")
            self.clearDisplay()
            self.displayText(
                "Hi, my",
                WHITE,
                self.display.width // 2,
                self.display.height // 3,
                FONT_SCALE_LARGE,
            )

        elif ticks == REFRESH_RATE:
            # self.clearDisplay()
            self.displayText(
                "name is",
                WHITE,
                self.display.width // 2,
                2 * self.display.height // 3,
                FONT_SCALE_LARGE,
            )

        elif ticks == REFRESH_RATE * 2:
            self.clearDisplay()
            self.displayText(
                "DIVY",
                WHITE,
                self.display.width // 2,
                self.display.height // 2,
                FONT_SCALE_EXTRA_LARGE,
            )

    def displayEnding(self, ticks):
        if ticks == 0:
            self.clearDisplay()
            self.displayText(
                "THANK YOU",
                WHITE,
                self.display.width // 2,
                self.display.height // 2,
                FONT_SCALE_LARGE,
            )
        elif ticks == REFRESH_RATE:
            self.displayText(
                "____",
                BLACK,
                self.display.width // 2,
                2 * self.display.height // 3,
                FONT_SCALE_LARGE,
            )
        elif ticks == REFRESH_RATE * 2:
            self.clearDisplay()
            self.displayText(
                "[^] [^]",
                BLACK,
                self.display.width // 2,
                self.display.height // 3,
                FONT_SCALE_LARGE,
            )
        elif ticks == REFRESH_RATE * 3:
            self.displayText(
                "O",
                BLACK,
                self.display.width // 2,
                2 * self.display.height // 3,
                FONT_SCALE_LARGE,
            )

    def displayAsciiFace(self, ticks):
        """
        Animation time is 3 seconds, but it can be stopped in the middle
        """
        if ticks == 1:
            # self.clearDisplay()
            self.color_bitmap.fill(1)
            self.displayText(
                "[||] [||]",
                BLACK,
                self.display.width // 2,
                self.display.height // 3,
                FONT_SCALE_LARGE,
            )
        elif ticks == REFRESH_RATE:
            self.displayText(
                "____",
                BLACK,
                self.display.width // 2,
                2 * self.display.height // 3,
                FONT_SCALE_LARGE,
            )
        elif ticks == REFRESH_RATE * 2:
            self.clearDisplay()
            self.displayText(
                "[X] [X]",
                BLACK,
                self.display.width // 2,
                self.display.height // 3,
                FONT_SCALE_LARGE,
            )
        elif ticks == REFRESH_RATE * 3:
            self.displayText(
                "O",
                BLACK,
                self.display.width // 2,
                2 * self.display.height // 3,
                FONT_SCALE_LARGE,
            )

    def displayColorFace(self, ticks):
        """
        Only one frame
        """
        if ticks == 1:
            self.clearDisplay()
            palette = displayio.Palette(3)
            palette[0] = WHITE
            palette[1] = BLACK
            palette[2] = RED

            left_eye = vectorio.Circle(
                pixel_shader=palette,
                radius=20,
                x=self.display.width // 3,
                y=self.display.height // 3,
            )
            left_pupil = vectorio.Circle(
                pixel_shader=palette,
                radius=10,
                x=self.display.width // 3,
                y=self.display.height // 3,
                color_index=1,
            )

            # points for a triangle (nose)
            points = [
                (120, 65),  # top middle
                (110, 75),  # left bottom
                (130, 75),  # left right
            ]
            nose = vectorio.Polygon(
                pixel_shader=palette, points=points, x=0, y=0, color_index=2
            )

            right_eye = vectorio.Circle(
                pixel_shader=palette,
                radius=20,
                x=2 * self.display.width // 3,
                y=self.display.height // 3,
            )
            right_pupil = vectorio.Circle(
                pixel_shader=palette,
                radius=10,
                x=2 * self.display.width // 3,
                y=self.display.height // 3,
                color_index=1,
            )
            mouth = vectorio.Rectangle(
                pixel_shader=palette,
                width=self.display.width // 2,
                height=self.display.height // 7,
                x=self.display.width // 4,
                y=self.display.height // 4 * 3,
            )

            self.splash.append(left_eye)
            self.splash.append(left_pupil)
            self.splash.append(right_eye)
            self.splash.append(right_pupil)
            self.splash.append(mouth)
            self.splash.append(nose)

    def displayArrows(self, ticks):
        """
        Arrow animation - left and right, switches constantly every 1 second
        """
        palette = displayio.Palette(3)
        palette[0] = CYAN
        palette[1] = MAGENTA
        palette[2] = ORANGE

        # if ticks == 1:
        #     self.color_bitmap.fill(0)
        refresh = 1.3 * 2

        if ticks % int(REFRESH_RATE * refresh) == 1:
            self.clearDisplay()
            # self.color_bitmap.fill(0)
            # points for a triangle (nose)
            points = [
                (140, 30),
                (220, (105 + 30) // 2),
                (140, 105),
            ]  # top  # right  # bottom
            right_triangle = vectorio.Polygon(
                pixel_shader=palette, points=points, x=0, y=0, color_index=2
            )
            right_rect = vectorio.Rectangle(
                pixel_shader=palette,
                width=self.display.width // 2,
                height=self.display.height // 4,
                x=20,
                y=(self.display.height // 2) - (self.display.height // 4) // 2,
            )
            self.splash.append(right_rect)
            self.splash.append(right_triangle)

        elif ticks % int(REFRESH_RATE * refresh / 2) == 1:
            self.clearDisplay()
            # self.color_bitmap.fill(0)
            # points for a triangle (nose)
            points = [
                (100, 30),
                (20, (105 + 30) // 2),
                (100, 105),
            ]  # top  # right  # bottom
            left_triangle = vectorio.Polygon(
                pixel_shader=palette, points=points, x=0, y=0, color_index=2
            )
            left_rect = vectorio.Rectangle(
                pixel_shader=palette,
                width=self.display.width // 2,
                height=self.display.height // 4,
                x=100,
                y=(self.display.height // 2) - (self.display.height // 4) // 2,
            )
            self.splash.append(left_rect)
            self.splash.append(left_triangle)

    def displayRainbowStreamManual(self, ticks):
        # initialize palette
        if ticks == 1:
            print("displaying rainbow")
            color_palette = displayio.Palette(7)
            color_list = [RED, ORANGE, YELLOW, GREEN, BLUE, INDIGO, VIOLET]

            for i in range(len(color_list)):
                color_palette[i] = color_list[i]

            for i in range(7):  # colors_list.len
                bmp_name = "temp_bmp_" + str(i)
                sprite_name = "temp_sprite_" + str(i)
                bmp_name = displayio.Bitmap(
                    self.display.width // 7, self.display.height, 7
                )
                bmp_name.fill(i)
                sprite_name = displayio.TileGrid(
                    bmp_name,
                    pixel_shader=color_palette,
                    tile_width=self.display.width // 7,
                    tile_height=self.display.height,
                    x=i * (self.display.width // 7),
                    y=0,
                )
                self.rainbow.append(bmp_name)
                self.splash.append(sprite_name)

        # updates
        elif ticks % (REFRESH_RATE / 5) == 0:
            self.rainbow_counter += 1
            for element in range(len(self.rainbow)):
                self.rainbow[element].fill((element + self.rainbow_counter) % 7)

    def displayColorBlocks(self):
        # Draw a smaller inner rectangle
        inner_bitmap = displayio.Bitmap(
            self.display.width - BORDER * 2, self.display.height - BORDER * 2, 1
        )
        inner_palette = displayio.Palette(1)
        inner_palette[0] = RED
        inner_sprite = displayio.TileGrid(
            inner_bitmap, pixel_shader=inner_palette, x=BORDER, y=BORDER
        )
        self.splash.append(inner_sprite)

    def displayText(self, text: str, c, x: int, y: int, font_scale: int):
        """Display a coloured string of text at an (x,y) location on the display
        @param str: the string to print
        @param c: the color of the text (ex: 0xFFFFFF)
        @param x: x location for the text to be displayed. 0 <= x <= 135
        @param y: y location for the text to be displayed. 0 <= y <= 240
        """
        text_area = label.Label(terminalio.FONT, text=text, color=c)
        text_width = text_area.bounding_box[2] * font_scale
        text_group = displayio.Group(
            scale=font_scale,
            x=x - text_width // 2,
            y=y,
        )
        text_group.append(text_area)
        self.splash.append(text_group)

    def displayRobotFaces(self, ticks):
        """Displays color face then ascii face then color face then ascii face
        Ascii face has two frames, whereas color face has one
        """
        if ticks % (REFRESH_RATE * 3) == 1:
            self.color_bitmap.fill(0)
            self.displayColorFace(0)
        elif ticks % (REFRESH_RATE * 3) == 101:
            self.clearDisplay()
            self.color_bitmap.fill(1)
            self.displayAsciiFace(1)
        elif ticks % (REFRESH_RATE * 3) == 201:
            self.displayAsciiFace(REFRESH_RATE)

    # """
    # Superloop
    # """
    # def refresh(self):
    #     while True:
    #         print("Code starting")

    #         self.displayIntro(5)

    #         self.displayDoge(5)

    #         self.displayArrows()

    #         self.displayRainbowStreamManual()

    #         self.color_bitmap.fill(0)  # fill background black
    #         self.displayColorFace()

    #         self.color_bitmap.fill(1)  # fill background white
    #         self.displayAsciiFace()
