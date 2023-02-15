# Group: 24
# Names: Divy, Elio, Kelvin, Matthew

import board
import digitalio
import time

"""
Keypad code for our second Pico board. Reads input from the keypad
and prints the corresponding number to the serial console which is
read by the connected computer (see serial_keypad.py).
"""

# Keypad pin declarations
pRow0 = digitalio.DigitalInOut(board.GP0)
pRow1 = digitalio.DigitalInOut(board.GP1)
pRow2 = digitalio.DigitalInOut(board.GP2)
pRow3 = digitalio.DigitalInOut(board.GP3)
pCol0 = digitalio.DigitalInOut(board.GP4)
pCol1 = digitalio.DigitalInOut(board.GP5)
pCol2 = digitalio.DigitalInOut(board.GP6)

# Keypad pin setup
pRow0.direction = digitalio.Direction.INPUT
pRow1.direction = digitalio.Direction.INPUT
pRow2.direction = digitalio.Direction.INPUT
pRow3.direction = digitalio.Direction.INPUT
pCol0.direction = digitalio.Direction.OUTPUT
pCol1.direction = digitalio.Direction.OUTPUT
pCol2.direction = digitalio.Direction.OUTPUT

# Keypad pull-up setup
pRow0.pull = digitalio.Pull.UP
pRow1.pull = digitalio.Pull.UP
pRow2.pull = digitalio.Pull.UP
pRow3.pull = digitalio.Pull.UP
pCol0.value = True
pCol1.value = True
pCol2.value = True

while True:
    # Check 1, 4, 7, *
    pCol0.value = False
    pCol1.value = True
    pCol2.value = True
    if pRow0.value == False:
        print("1")
    elif pRow1.value == False:
        print("4")
    elif pRow2.value == False:
        print("7")
    elif pRow3.value == False:
        print("*")
    time.sleep(0.1)

    # Check 2, 5, 8, 0
    pCol0.value = True
    pCol1.value = False
    pCol2.value = True
    if pRow0.value == False:
        print("2")
    elif pRow1.value == False:
        print("5")
    elif pRow2.value == False:
        print("8")
    elif pRow3.value == False:
        print("0")
    time.sleep(0.1)

    # Check 3, 6, 9, #
    pCol0.value = True
    pCol1.value = True
    pCol2.value = False
    if pRow0.value == False:
        print("3")
    elif pRow1.value == False:
        print("6")
    elif pRow2.value == False:
        print("9")
    elif pRow3.value == False:
        print("#")
    time.sleep(0.1)
