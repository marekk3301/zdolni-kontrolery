import time
import board
import analogio
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

# Dioda LED
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

# Niektóre sensory potrzebują zasilania, dla fotorezystora nie jest to potrzebne
plus = digitalio.DigitalInOut(board.A1)
plus.direction = digitalio.Direction.OUTPUT
plus.value = True

# Fotorezystor
sensor = analogio.AnalogIn(board.A0)

# Klawiatura
keyboard = Keyboard(usb_hid.devices)

THRESHOLD = 600  # Adjust this threshold based on testing

while True:
    light_level = sensor.value  # Odczytaj aktualną wartość sensora
    print("Light level:", light_level)  # Wypisz wartość w terminalu
    
    if light_level > THRESHOLD:  # Jeśli sensor jest zasłonięty (wartość jest większa niż 600)
        led.value = True  
        keyboard.press(Keycode.SPACE)  # Wciskamy spację na klawiaturze
        print("Pressed SPACE")
    else:
        led.value = False 
        keyboard.release_all()
    
    time.sleep(0.1)
