# Group: 24
# Names: Divy, Elio, Kelvin, Matthew

## Proof of concept for a 4x3 keypad (not yet in use)

import board
import pwmio
import digitalio
import time

# keypad pin declarations
pRow0 = digitalio.DigitalInOut(board.GP0)
pRow1 = digitalio.DigitalInOut(board.GP1)
pRow2 = digitalio.DigitalInOut(board.GP2)
pRow3 = digitalio.DigitalInOut(board.GP3)
pCol0 = digitalio.DigitalInOut(board.GP4)
pCol1 = digitalio.DigitalInOut(board.GP5)
pCol2 = digitalio.DigitalInOut(board.GP6)

# keypad pin setup
pRow0.direction = digitalio.Direction.INPUT
pRow1.direction = digitalio.Direction.INPUT
pRow2.direction = digitalio.Direction.INPUT
pRow3.direction = digitalio.Direction.INPUT
pCol0.direction = digitalio.Direction.OUTPUT
pCol1.direction = digitalio.Direction.OUTPUT
pCol2.direction = digitalio.Direction.OUTPUT

# keypad puullup setup
pRow0.pull = digitalio.Pull.UP
pRow1.pull = digitalio.Pull.UP
pRow2.pull = digitalio.Pull.UP
pRow3.pull = digitalio.Pull.UP
pCol0.value = True
pCol1.value = True
pCol2.value = True

while True:
    # check 1, 4, 7, *
    pCol0.value = False
    pCol1.value = True
    pCol2.value = True
    if pRow0.value == False:
        print("1 pressed")
    elif pRow1.value == False:
        print("4 pressed")
    elif pRow2.value == False:
        print("7 pressed")
    elif pRow3.value == False:
        print("* pressed")
    time.sleep(0.1)
    
    # check 2, 5, 8, 0
    pCol0.value = True
    pCol1.value = False
    pCol2.value = True
    if pRow0.value == False:
        print("2 pressed")
    elif pRow1.value == False:
        print("5 pressed")
    elif pRow2.value == False:
        print("8 pressed")
    elif pRow3.value == False:
        print("0 pressed")
    time.sleep(0.1)
    
    # check 3, 6, 9, #
    pCol0.value = True
    pCol1.value = True
    pCol2.value = False
    if pRow0.value == False:
        print("3 pressed")
    elif pRow1.value == False:
        print("6 pressed")
    elif pRow2.value == False:
        print("9 pressed")
    elif pRow3.value == False:
        print("# pressed")
    time.sleep(0.1)
