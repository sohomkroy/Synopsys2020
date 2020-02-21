# This python file will read inputs from the gamepad, allowing a person to easily control the car with
# the camera and other components. This file will be imported by other files

import inputs

class GamePad():

    dpad_up: bool = False
    dpad_left: bool = False
    dpad_right: bool = False
    dpad_down: bool = False

    button_up: bool = False
    button_left: bool = False
    button_right: bool = False
    button_down: bool = False

    left_stick_x: float = 0
    left_stick_y: float = 0

    right_stick_x: float = 0
    right_stick_y: float = 0

    def __init__(self):
        pass

    def poll_gamepad(self):
        events = inputs.get_gamepad()
        for event in events:
            if (event.code == "BTN_NORTH"):
                 button_up = event.state == 1
            if (event.code == "BTN_SOUTH"):
                 button_down = event.state == 1
            if (event.code == "BTN_LEFT"):
                 button_left = event.state == 1
            if (event.code == "BTN_RIGHT"):
                 button_right = event.state == 1




while True:
    events = inputs.get_gamepad()
    x = 0
    y = 0
    for event in events:
        if event.code == "ABS_RX":
            x = event.state;
        if event.code == "ABS_RY":
            y = event.state;
        #print(event.code, event.state/32768)
    print(x, y)
