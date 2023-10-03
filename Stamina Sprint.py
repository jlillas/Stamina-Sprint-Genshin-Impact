import keyboard
import time
import sys

count = 0
running = False
refresh_rate = 0.01

while True:
    if keyboard.is_pressed("q"):
        sys.exit()

    if keyboard.is_pressed("h"):
        count += 1
        if count == 1:
            running = True
        elif count == 2:
            count = 0
            running = False
    
    if running:
        keyboard.press_and_release("w")
        keyboard.press_and_release("shift")
    
    time.sleep(refresh_rate)
