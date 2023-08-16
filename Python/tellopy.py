from djitellopy import tello
from time import sleep
import cv2

myDrone = tello.Tello()
myDrone.connect()
myDrone.stream_on()

print("Battery: " + myDrone.get_battery())
print("Height: " + myDrone.get_height())
print("Temprature: " + myDrone.get_temperature())
print("Speed (X) : " + myDrone.get_speed_x())
print("Speed (y) : " + myDrone.get_speed_y())


# here parameter is in cm.
# myDrone.takeoff()
# myDrone.rotate_counter_clockwise(90)
# myDrone.move_forward(100)
# myDrone.move_back(100)
# myDrone.move_left(100)
# myDrone.move_right(100)
# myDrone.land()


# Get Video
while True:
    img = myDrone.get_frame_read().frame
    img = cv2.resize(370,240)
    cv2.imshow("Image",img)
    cv2.waitKey(1)


# DJI Tello drone python interface using the official Tello SDK and Tello EDU SDK.  
# https://github.com/damiafuentes/DJITelloPy