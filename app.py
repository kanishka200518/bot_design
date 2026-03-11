from flask import Flask, render_template, Response, jsonify
import config

app = Flask(__name__)

# These will be assigned by main.py
vision_system = None
robot_state = {
    "status": "Initializing...",
    "run_time": 0.0, # seconds
    "detections": []
}

@app.route('/')
def index():
    return render_template('index.html')

def gen_frames():
    """Generator for MJPEG streaming."""
    while True:
        if vision_system is None:
            continue
            
        frame_bytes = vision_system.read_frame_jpeg()
        if frame_bytes:
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/api/state')
def get_state():
    """Endpoint for the dashboard to poll the latest robot status dynamically."""
    if vision_system is not None:
        robot_state['detections'] = vision_system.get_detections()
        
    return jsonify(robot_state)

def start_server():
    """Start the Flask server on 0.0.0.0 to be accessible across the network."""
    app.run(host='0.0.0.0', port=config.FLASK_PORT, debug=False, use_reloader=False)

if __name__ == '__main__':
    start_server()
