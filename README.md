# 21_blink_led
Raspberry pi

# Raspberry Pi LED Blinking Project

## Overview
This project demonstrates how to control two LEDs using a Raspberry Pi. The LEDs will blink alternately with a delay of one second between each blink.

## Requirements
- Raspberry Pi (any model with GPIO pins)
- Two LEDs
- Two 220-ohm resistors
- Breadboard and jumper wires
- Python 3
- RPi.GPIO library

## Circuit Diagram
Connect the components as follows:
- Connect the anode (longer leg) of the first LED to GPIO pin 12 through a 220-ohm resistor.
- Connect the cathode (shorter leg) of the first LED to a ground (GND) pin.
- Connect the anode (longer leg) of the second LED to GPIO pin 13 through a 220-ohm resistor.
- Connect the cathode (shorter leg) of the second LED to a ground (GND) pin.

## Installation
1. Install the RPi.GPIO library if not already installed. You can install it using pip:
   ```bash
   pip install RPi.GPIO
   ```

## Code Explanation
The Python code provided in this project is used to control the LEDs connected to GPIO pins 12 and 13 on the Raspberry Pi.

1. **Import Libraries**
   ```python
   import RPi.GPIO as GPIO
   import time
   ```

2. **Setup GPIO Mode**
   ```python
   GPIO.setmode(GPIO.BCM)
   ```

3. **Define GPIO Pins**
   ```python
   ledPinOne = 12
   ledPinTwo = 13
   ```

4. **Setup GPIO Pins as Outputs**
   ```python
   GPIO.setup(ledPinOne, GPIO.OUT)
   GPIO.setup(ledPinTwo, GPIO.OUT)
   ```

5. **Main Loop**
   The loop alternates the state of the two LEDs with a 1-second delay between changes.
   ```python
   try:
       while True:
           GPIO.output(ledPinOne, GPIO.HIGH)
           GPIO.output(ledPinTwo, GPIO.LOW)
           time.sleep(1)
           GPIO.output(ledPinOne, GPIO.LOW)
           GPIO.output(ledPinTwo, GPIO.HIGH)
           time.sleep(1)
   except KeyboardInterrupt:
       print("\nExiting program\n")
       GPIO.cleanup()
       exit()
   ```

## Running the Code
1. Connect the LEDs and resistors to the Raspberry Pi as described in the circuit diagram.
2. Copy the provided Python code into a file, e.g., `led_blink.py`.
3. Run the Python script:
   ```bash
   python led_blink.py
   ```
4. The LEDs should start blinking alternately. Press `Ctrl+C` to stop the program.

## Cleanup
When the program is interrupted (e.g., by pressing `Ctrl+C`), the `except` block will execute, printing a message and cleaning up the GPIO settings to prevent issues in future GPIO usage.

```python
except KeyboardInterrupt:
    print("\nExiting program\n")
    GPIO.cleanup()
    exit()
```

## Notes
- Ensure that the GPIO pins and connections are correctly set up to avoid damaging the Raspberry Pi or the LEDs.
- The `time.sleep(1)` function creates a 1-second delay between each state change of the LEDs.

Enjoy experimenting with your Raspberry Pi and LEDs!
