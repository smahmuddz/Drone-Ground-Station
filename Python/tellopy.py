from djitellopy import Tello
from time import sleep
import cv2

myDrone = Tello()
myDrone.connect()
myDrone.streamon()  # Use streamon() instead of stream_on()

print("Battery: " + str(myDrone.get_battery()))  # Convert battery value to string
print("Height: " + str(myDrone.get_height()))    # Convert height value to string
print("Temperature: " + str(myDrone.get_temperature()))  # Corrected 'Temprature' to 'Temperature'
print("Speed (X): " + str(myDrone.get_speed_x()))  # Convert speed_x value to string
print("Speed (Y): " + str(myDrone.get_speed_y()))  # Convert speed_y value to string

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
    img = cv2.resize(img, (640, 480))  # Corrected the resize parameters
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Exit loop when 'q' key is pressed
        break

myDrone.streamoff()  # Use streamoff() instead of stream_on()
cv2.destroyAllWindows()

# DJI Tello drone python interface using the official Tello SDK and Tello EDU SDK.
# https://github.com/damiafuentes/DJITelloPy
