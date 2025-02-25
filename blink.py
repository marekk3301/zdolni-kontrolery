import time
import board
import digitalio

led = digitalio.DigitalInOut(board.LED) 
led.direction = digitalio.Direction.OUTPUT

while True:
   print("led on") # Drukujemy informację w terminalu
   led.value = True  # Włączamy led
   time.sleep(1)   # i czekamy 1 sekundę.
   led.value = False  # Po sekundzie wyłączamy
   time.sleep(1)   # i znowu czekamy
