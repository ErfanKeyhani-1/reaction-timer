# THIS IS PYTHON NOW

from microbit import *
import random
import time

while True:
    display.show("3")
    sleep(1000)
    display.show("2")
    sleep(1000)
    display.show("1")
    sleep(1000)
    display.clear()

    # Wait a random time before flashing
    sleep(random.randint(1000, 4000))

    # Flash the screen
    display.show(Image.SQUARE)
    start_time = running_time()

    # Wait for button A press
    while not button_a.is_pressed():
        sleep(10)

    end_time = running_time()
    reaction_time = end_time - start_time

    # Show reaction time
    display.scroll(str(reaction_time))

    # Pause and reset for next round
    sleep(2000)
    display.clear()
