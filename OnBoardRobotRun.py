import cv2
from OnGroundRobot import Gamepad
from OnGroundRobot import Visualizer
from OnGroundRobot import FireBaseInterfacer


gp = Gamepad.GamePad()
vis = Visualizer.Visualizer("")
db = FireBaseInterfacer.

light_on:bool = False

while True:

    if (gp.button_right):
        if light_on:
            light_on = False
        else:
            light_on = True


    frame = vis.get_frame(gp.left_stick_y, gp.right_stick_x, 0, 0, light_on, "Home Wifi", light_on, 0)
    if frame is None:
        break
    cv2.imshow("camera stream", frame)


vis.release_visualizer()

