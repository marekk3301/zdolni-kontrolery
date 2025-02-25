import time
import board
import digitalio

# Dioda LED
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

# Przycisk
button = digitalio.DigitalInOut(board.GP3) # Tu trzeba podać numer pinu do którego wpinamy przycisk
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

while True:
    if not button.value:  # Sprawdzamy czy przycisk jest wciśnięty
        led.value = True  # Jeśli jest to włączamy led
        print("click") # i wypisujemy informacje w terminalu
    else:
        led.value = False  # Jeśli nie to wyłączamy
    time.sleep(0.1)  # zatrzymujemy się na sekundę żeby przycisk lepiej działał
