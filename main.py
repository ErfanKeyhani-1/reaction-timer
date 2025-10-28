let startTime = 0
let endTime = 0
let reactionTime = 0

input.onButtonPressed(Button.A, function () {
    if (startTime > 0 && endTime == 0) {
        // Stop timer
        endTime = control.millis()
        reactionTime = endTime - startTime
        basic.showNumber(reactionTime)
    }
})

basic.forever(function () {
    basic.showString("3")
    basic.pause(1000)
    basic.showString("2")
    basic.pause(1000)
    basic.showString("1")
    basic.pause(1000)

    // Wait random time before flash
    basic.clearScreen()
    basic.pause(randint(1000, 4000))

    // Flash the screen
    basic.showIcon(IconNames.Square)
    startTime = control.millis()
    endTime = 0

    // Wait for user press
    while (endTime == 0) {
        basic.pause(50)
    }

    // Show result for a bit, then restart
    basic.pause(2000)
    basic.clearScreen()
    startTime = 0
    endTime = 0
})
