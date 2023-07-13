from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO, emit
import paho.mqtt.client as mqtt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'comnet'
socketio = SocketIO(app)
data = ''

@app.route('/')
def index():
    hostname1 = 'camera'
    hostname2 = 'motor1'
    hostname3 = 'motor2'

    is_reachable1 = perform_ping(hostname1) and perform_ping(hostname2)
    is_reachable2 = perform_ping(hostname3)

    return render_template('index.html', bin1_reachable=is_reachable1, bin2_reachable=is_reachable2)

@app.route('/bin1')
def bin1():
    hostname1 = 'camera'
    hostname2 = 'motor1'
    hostname3 = 'motor2'

    is_reachable1 = perform_ping(hostname1) and perform_ping(hostname2)
    is_reachable2 = perform_ping(hostname3)

    if is_reachable1:
        return render_template('bin1.html', bin1_reachable=is_reachable1, bin2_reachable=is_reachable2)
    else:
        # return render_template('bin1.html', bin1_reachable=is_reachable1, bin2_reachable=is_reachable2)
        return render_template('offline.html')

@app.route('/bin2')
def bin2():
    hostname1 = 'camera'
    hostname2 = 'motor1'
    hostname3 = 'motor2'

    is_reachable1 = perform_ping(hostname1) and perform_ping(hostname2)
    is_reachable2 = perform_ping(hostname3)

    if is_reachable2:
        return render_template('bin2.html', bin1_reachable=is_reachable1, bin2_reachable=is_reachable2)
    else:
        return render_template('offline.html')
        # return render_template('bin2.html', bin1_reachable=is_reachable1, bin2_reachable=is_reachable2)

def perform_ping(hostname):
    # Implement the ping operation using a library or system command
    # Return True if the hostname is reachable, False otherwise
    # Example using the 'ping' command on Linux:
    import subprocess
    result = subprocess.run(['ping', '-c', '1', '-W', '1', hostname], capture_output=True)
    return result.returncode == 0

@app.route('/ping/<hostname>')
def ping(hostname):
    status = 'online' if perform_ping(hostname) else 'offline'
    return jsonify({'status': status})

@socketio.on('message')
def handle_message(message):
    global data
    data = message
    emit('update', data)

@socketio.on('mqtt_publish')
def handle_mqtt_publish(data):
    message = data['message']
    topic = data['topic']  # Use the topic 'bin2'

    # Publish MQTT message based on the received data
    client.publish(topic, message)


# Define callback function for received messages
def on_message(client, userdata, msg):
    topic = msg.topic
    payload = msg.payload.decode()
    message = {'topic': topic, 'payload': payload}
    # Process received message
    print(f"Received message: Topic={topic}, Payload={payload}")
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
broker_address = "central"
broker_port = 1883
client.connect(broker_address, broker_port)

# Subscribe to topic
topic1 = "trash/plastic"
topic2 = "trash/general"
topic4 = "temp/alan"
topic5 = "temp/jj"
topic6 = "temp/nick"
topic7 = "temp/travis"
topic8 = "camera"
client.subscribe(topic1)
client.subscribe(topic2)
client.subscribe(topic4)
client.subscribe(topic5)
client.subscribe(topic6)
client.subscribe(topic7)
client.subscribe(topic8)

# Start the MQTT client loop
client.loop_start()

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0")
# To run flask app, use this command
# flask run --debug -h ( ipv4 address )
# Publishing Central PI temperature
