from flask import Flask, Response, request
from djitellopy import Tello
import cv2
import threading

app = Flask(__name__)
myDrone = Tello()
myDrone.connect()
myDrone.streamon()

# Flag to control the streaming loop
streaming = True

def generate_frames():
    while streaming:
        img = myDrone.get_frame_read().frame
        img = cv2.resize(img, (640, 480))
        _, buffer = cv2.imencode('.jpg', img)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/send-command', methods=['POST'])
def send_command():
    try:
        command = request.form.get('command')
        # Process the command here
        print(command)
        response_data = "Command received: " + command
        return Response(response_data, content_type='text/plain; charset=UTF-8')
    except Exception as e:
        return Response("Error processing command: " + str(e), content_type='text/plain; charset=UTF-8')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
