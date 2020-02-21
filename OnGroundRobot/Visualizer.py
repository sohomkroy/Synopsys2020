import cv2
import numpy as np


#TODO Add visualizer for microphone leve, gase level, and motion detecteed
class Visualizer():
    height: int = 480
    width: int = 640
    url: str = None
    capture = None

    def __init__(self, url):
        self.capture = cv2.VideoCapture(0)
        # self.capture = cv2.VideoCapture(self.url)

    def get_frame(self, forward_amount: int, turning_amount: int,
                  microphone_level: float, gas_level: float, light_on: bool,
                  wifi_network: str, motion_detected: bool):
        green_light = cv2.imread("D:\Sohom\Programming_Data\Synopsys2020\OnGroundRobot\green_light.png")
        green_light = cv2.resize(green_light, (30, 40), interpolation=cv2.INTER_AREA)

        ret, frame = self.capture.read()
        if not ret: return None

        frame = cv2.resize(frame, (self.width, self.height), interpolation=cv2.INTER_AREA)

        # draw forward backward arrow
        start_point = (60, 350)
        end_point = (90, int(350 - forward_amount * 60))
        color = (255, 255, 0)
        thickness = -1

        if (forward_amount != 0):
            frame = cv2.rectangle(frame, start_point, end_point, color, thickness)

            pts = np.array([[75 - 40, 350 - forward_amount * 60], [75 + 40, 350 - forward_amount * 60],
                            [75, 350 - forward_amount * 120]], np.int32)
            pts = pts.reshape((-1, 1, 2))
            frame = cv2.fillPoly(frame, [pts], (255, 255, 0))

        # draw forward backward arrow
        start_point = (475, 360)
        end_point = (int(475-turning_amount*60), 390)
        color = (255, 255, 0)
        thickness = -1
        if (turning_amount != 0):
            frame = cv2.rectangle(frame, start_point, end_point, color, thickness)
            pts = np.array([[475 - turning_amount * 60, 375 - 40], [474 - turning_amount * 60, 375 + 40,],
                           [475 - turning_amount * 120, 375]], np.int32)
            pts = pts.reshape((-1, 1, 2))
            frame = cv2.fillPoly(frame, [pts], (255, 255, 0))

        #write text for wifi network
        frame = cv2.putText(frame, wifi_network, (460, 30), cv2.FONT_HERSHEY_DUPLEX, .8,
                            (0, 0, 255), 1)

        # add graphic for light
        if light_on:
            x_offset = 425
            y_offset = 0
            frame[y_offset:y_offset + green_light.shape[0], x_offset:x_offset + green_light.shape[1]] = green_light

        # add graphic for gas reading



        if cv2.waitKey(1) & 0xFF == ord('q'):
            return None
        return frame

    def release_visualizer(self):
        self.capture.release()
        cv2.destroyAllWindows()


def main():
    vis = Visualizer("")
    count: float = 0;
    direction: int = 1
    while True:
        frame = vis.get_frame(count, count, 0, 0, True, "Home Wifi", True, 0)
        if frame is None:
            break
        cv2.imshow("camera stream", frame)

        if count > 1:
            direction = -1
        if count < -1:
            direction = 1

        count += .05 * direction

    vis.release_visualizer()


if __name__ == "__main__":
    main()
