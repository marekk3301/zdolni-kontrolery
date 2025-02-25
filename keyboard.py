import time
import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

# Dioda LED
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

# Przycisk
button = digitalio.DigitalInOut(board.GP1)  # Tu trzeba podać numer pinu do którego wpinamy przycisk
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

# Klawiatura
keyboard = Keyboard(usb_hid.devices)

while True:
    if not button.value:  # Sprawdzamy czy przycisk jest wciśnięty
        keyboard.press(Keycode.SPACE)  # Jeśli jest to wciskamy spację na klawiaturze
        led.value = True  # włączamy led
        print("click") # i wypisujemy informacje w terminalu
    else:
        keyboard.release_all() # Jeśli nie to puszczamy spacje (wszystkie wciśnięte klawisze)
        led.value = False  # i wyłączamy led
    time.sleep(0.1)  # zatrzymujemy się na sekundę żeby przycisk lepiej działał
