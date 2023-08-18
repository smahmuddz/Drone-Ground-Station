from flask import Flask, Response
from djitellopy import Tello
import cv2

app = Flask(__name__)
myDrone = Tello()
myDrone.connect()
myDrone.streamon()

def generate_frames():
    while True:
        img = myDrone.get_frame_read().frame
        img = cv2.resize(img, (640, 480))
        _, buffer = cv2.imencode('.jpg', img)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
