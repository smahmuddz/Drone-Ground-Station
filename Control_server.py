from flask import Flask, Response
from djitellopy import Tello
import cv2
from time import *
app = Flask(__name__)
# myDrone = Tello()
# myDrone.connect()

@app.route('/')
def index():
    return open("index.html").read()

@app.route('/takeoff', methods=['get'])
def takeoff():
    print("Takeoff Button Pressed")
    sleep(4)  # Adjust sleep duration as needed
    return "take off"

@app.route('/land', methods=['get'])
def land():
    print("Land Button Pressed")
    return "Land"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
