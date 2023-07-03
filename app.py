from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import paho.mqtt.client as mqtt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'comnet'
socketio = SocketIO(app)
data = ''

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/camera')
def camera():
    return render_template('camera.html')

@app.route('/status')
def status():
    return render_template('status.html')

@app.route('/trash')
def trash():
    return render_template('trash1.html',data=data)
    
@app.route('/data')
def data():
    return render_template('data.html')
    
@socketio.on('message')
def handle_message(message):
    global data
    data = message
    emit('update', data)

# Define callback function for received messages
def on_message(client, userdata, msg):
    message = msg.payload.decode()
    # Process received message
    print("Recevied message:", msg.payload.decode())
    socketio.emit('update', message)
    
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected!")
    else:
        print("Connection failed!")

# Create an MQTT client instance
client = mqtt.Client()

# Assign callback function
client.on_connect = on_connect
client.on_message = on_message

# Set username and password
username = "admin"
password = "password"
client.username_pw_set(username, password)

# Connect to the MQTT broker
broker_address = "192.168.10.191"
broker_port = 1883
client.connect(broker_address, broker_port)

# Subscribe to topic
topic1 = "/trash"
client.subscribe(topic1)

# Start the MQTT client loop
client.loop_start()

if __name__ == "__main__":
    socketio.run(app)
# To run flask app, use this command
# flask run --debug -h ( ipv4 address )
