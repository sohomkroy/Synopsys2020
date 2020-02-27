import numpy as np
import cv2
import time

cap = cv2.VideoCapture("D:\Sohom\Programming_Data\Synopsys2020\RealtimeObjectDetection\SampleVideo\\video1.mp4")
time.sleep(5)
print("got stream")
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    print(ret)

    # Our operations on the frame come here
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()