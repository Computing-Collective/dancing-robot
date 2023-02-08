from lcd import *

"""
Instantiate the LCD
"""

# Release any resources currently in use for the displays
displayio.release_displays()

# set up GPIO
tft_dc = board.GP8
tft_cs = board.GP9
spi_clk = board.GP10
spi_mosi = board.GP11
tft_res = board.GP12

spi = busio.SPI(spi_clk, MOSI=spi_mosi)

while not spi.try_lock():
    pass
spi.configure(baudrate=24000000)  # Configure SPI for 24MHz
spi.unlock()

display_bus = displayio.FourWire(spi, command=tft_dc, chip_select=tft_cs, reset=tft_res)

x = LCD(display_bus)

print("main")

x.refresh()
