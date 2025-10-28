#HERE IS THE DAMN PYTHON CODE

startTime = 0
endTime = 0
reactionTime = 0

def on_button_pressed_a():
    global endTime, reactionTime
    if startTime > 0 and endTime == 0:
        # Stop timer
        endTime = control.millis()
        reactionTime = endTime - startTime
        basic.show_number(reactionTime)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_forever():
    global startTime, endTime
    basic.show_string("3")
    basic.pause(1000)
    basic.show_string("2")
    basic.pause(1000)
    basic.show_string("1")
    basic.pause(1000)
    # Wait random time before flash
    basic.clear_screen()
    basic.pause(randint(1000, 4000))
    # Flash the screen
    basic.show_icon(IconNames.SQUARE)
    startTime = control.millis()
    endTime = 0
    # Wait for user press
    while endTime == 0:
        basic.pause(50)
    # Show result for a bit, then restart
    basic.pause(2000)
    basic.clear_screen()
    startTime = 0
    endTime = 0
basic.forever(on_forever)
