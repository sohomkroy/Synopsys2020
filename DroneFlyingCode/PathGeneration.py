import cv2
import numpy as np

img = cv2.imread("D:\Sohom\Programming_Data\Synopsys2020\DroneFlyingCode\Image\CreekSidePark.png")


scale_percent = 60 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
# resize image
img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
img = img[20:20+450, 50:50+330]

max_speed = 5 #ft per second

#lineThickness = 1
#cv2.line(img, (554, 500), (637, 500), (255,255,255), lineThickness)

scale  = 200/(637-554) #foor per pixel
feet_per_latitude = 364099.0681813498
feet_per_longitude = 292032.35603412613
lineThickness = 1
cv2.line(img, (0, 0), (0, 500), (255,255,255), lineThickness)
cv2.line(img, (int(50*scale), 0), (int(50*scale), 500), (255,255,255), lineThickness)
cv2.line(img, (int(100*scale), 0), (int(100*scale), 500), (255,255,255), lineThickness)
cv2.line(img, (int(150*scale), 0), (int(150*scale), 500), (255,255,255), lineThickness)

cv2.line(img, (0, 0), (350, 0), (255,255,255), lineThickness)
cv2.line(img, (0, int(50*scale)), (350, int(50*scale)), (255,255,255), lineThickness)
cv2.line(img, (0, int(100*scale)), (350, int(100*scale)), (255,255,255), lineThickness)
cv2.line(img, (0, int(150*scale)), (350, int(150*scale)), (255,255,255), lineThickness)
cv2.line(img, (0, int(200*scale)), (350, int(200*scale)), (255,255,255), lineThickness)



def fTP(feet):
    return int(feet*scale)

start_position = (fTP(30), fTP(25))
waypoint1 = (fTP(110), fTP(25))
waypoint2 = (fTP(110), fTP(75))
waypoint3 = (fTP(30), fTP(75))
end_position = (fTP(30), fTP(175))

start_position_ft = (30, 25)
waypoint1_ft = (110, 25)
waypoint2_ft = (110, 75)
waypoint3_ft = (30, 75)
end_position_ft = (30, 175)

cv2.line(img, start_position, waypoint1, (0,255,0), lineThickness)
cv2.line(img, waypoint1, waypoint2, (0,255,0), lineThickness)
cv2.line(img, waypoint2, waypoint3, (0,255,0), lineThickness)
cv2.line(img, waypoint3, end_position, (0,255,0), lineThickness)

def ft_to_deg(waypoint):
    return (37.316139+waypoint[0]*1/feet_per_longitude, -122.015967+waypoint[1]*1/feet_per_latitude)

waypoint_list_ft = (start_position_ft, waypoint1_ft, waypoint2_ft, waypoint3_ft, end_position_ft)
waypoint_list_deg = []

for waypoint in waypoint_list_ft:
    waypoint_list_deg.append(ft_to_deg(waypoint))

for pt in waypoint_list_deg:
    print(pt)



cv2.imshow('image-2',img)
cv2.waitKey(0)
cv2.destroyAllWindows()