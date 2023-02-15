# Project 1: Dancing Robot

Group: 24

Names: Divy, Elio, Kelvin, Matthew

## File Structure & Explanation

### Robot (Pico W)

* `[constants.py](/constants.py)` - A file that contains key constants used throughout the robot program. This includes the refresh rate and the URL for requesting moves from the server.
* `[main.py](/main.py)` - The main robot program that sets up pins, instantiates classes, and manages the timing of the robot.
* `[robot.py](/robot.py)` - A class that handles the robot's moves. This class handles the movement of the robot based on the current move as well as the timing with the LCD.
* `[lcd.py](/lcd.py)` - A class that handles the LCD screen on the robot. This class displays various animations synced to the various robot moves.
* `[led.py](/led.py)` - A class that handles the LED on the robot. This class turns on the LEDs in different sequences based on the current move.
* `[wireless.py](/wireless.py)` - A class that handles the wireless communication between the robot and the server. This class handles the request to the server for the next move and the response from the server with the next move.
* `[settings.toml](/settings.toml)` - A file that contains the wireless network credentials (name and password)

### Server Laptop

* `[server.py](/server.py)` - The main server program. This is the program that runs on the server laptop and handles all the communication between the server and the client.

### External Keypad (Pico H)

* `[keypad.py](/keypad.py)` - The main keypad program (named `main.py` when put on the Pico H). Continuously reads the keypad and sends the key pressed to the serial console.

### Pico H Laptop

* `[serial_keypad.py](/serial_keypad.py)` - A program that reads the serial console and sends the key pressed to the server.
