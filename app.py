import paho.mqtt.client as paho
import time
from flask import Flask, request
from flask_cors import CORS

def on_connect(client, userdata, flags, rc):
    print('CONNACK received with code %d.' % (rc))

def on_publish(client, userdata, mid):
    print("mid: "+str(mid))

mqclient = paho.Client()
mqclient.on_connect = on_connect
mqclient.on_publish = on_publish
mqclient.connect('broker.hivemq.com', 1883)


def on_connect(client, userdata, flags, rc):
  client.subscribe("mineqtt")

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/toToggle', methods=['POST'])
def to_toggle():
    if request.method == 'POST':
        data = request.form
        print(data)
        mqclient.loop_start()
        mqclient.publish("topic/subtopic/test", str(data), 1)
        mqclient.loop_stop()
        return "Você enviou: {data}"
    return "Apenas solicitações POST são permitidas aqui."

if __name__ == '__main__':
    app.run()

