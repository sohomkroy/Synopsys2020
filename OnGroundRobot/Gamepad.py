import pyxinput
from Util import MathUtil

#pyxinput.test_virtual()

class GamePad():
    gamepad = None
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
        self.gamepad = pyxinput.rController(1)

    def poll_gamepad(self):
        button_list: list = self.gamepad.buttons

        self.button_down = 'A' in button_list
        self.button_right = 'B' in button_list
        self.button_up = 'Y' in button_list
        self.button_left = 'X' in button_list

        self.dpad_down = 'DPAD_DOWN' in button_list
        self.dpad_left = 'DPAD_LEFT' in button_list
        self.dpad_right = 'DPAD_RIGHT' in button_list
        self.dpad_up = 'DPAD_UP' in button_list

        gamepad_scale_factor: int = 32768

        self.left_stick_x = (self.gamepad.gamepad.__getitem__("thumb_lx")-128)/gamepad_scale_factor
        self.left_stick_y = (self.gamepad.gamepad.__getitem__("thumb_ly")-128)/gamepad_scale_factor
        self.right_stick_x = (self.gamepad.gamepad.__getitem__("thumb_rx")-128)/gamepad_scale_factor
        self.right_stick_y = (self.gamepad.gamepad.__getitem__("thumb_ry")-128)/gamepad_scale_factor

        self.left_stick_x = MathUtil.clip(self.left_stick_x, -1, 1)
        self.left_stick_y = MathUtil.clip(self.left_stick_y, -1, 1)
        self.right_stick_x = MathUtil.clip(self.right_stick_x, -1, 1)
        self.right_stick_y = MathUtil.clip(self.right_stick_y, -1, 1)





def main():
    gamepad = GamePad()
    while True:
        #a = pyxinput.rController(1)
        #print(a.gamepad.__getitem__("thumb_rx"))
        gamepad.poll_gamepad()
        print(gamepad.left_stick_x, gamepad.left_stick_y)

if __name__ == "__main__":
    main()

