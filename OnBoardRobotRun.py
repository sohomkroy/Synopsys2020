import cv2
import math
from OnGroundRobot import Gamepad
from OnGroundRobot import Visualizer
from OnGroundRobot import FireBaseInterfacer


gp = Gamepad.GamePad()
vis = Visualizer.Visualizer("")

config = {
        "apiKey": "AIzaSyBBFze3rkgjPBwEkno8ZFOuHZLCWhbXstk",
        "authDomain": "synopsys2020-1.firebaseapp.com",
        "databaseURL": "https://synopsys2020-1.firebaseio.com/",
        "storageBucket": "synopsys2020-1.appspot.com"
    }

db = FireBaseInterfacer.FireBaseUpdater(config)

light_on:bool = False
left_stick_y: float = 0
right_stick_x: float = 0
data: dict = None

sound_level = 0

while True:

    gp.poll_gamepad()
    if (gp.button_right):
        if light_on:
            light_on = False
        else:
            light_on = True

    left_stick_y = gp.left_stick_y
    right_stick_x = gp.right_stick_x
    if (abs(left_stick_y)<.1):
        left_stick_y = 0
    if (abs(right_stick_x)<.1):
        right_stick_x = 0

    data = db.get_information()
    #data.get('MicrophoneLevel')
    frame = vis.get_frame(left_stick_y, -right_stick_x, math.sin(sound_level)/2+.5, data.get('GasLevel')/100, light_on, data.get('WifiNetwork'), data.get('MotionDetected'))
    db.write_information(left_stick_y, right_stick_x, light_on)


    if (frame is None) or (cv2.waitKey(1) & 0xFF == ord('q')):
        break
    cv2.imshow("camera stream", frame)

    sound_level+=.1




vis.release_visualizer()

