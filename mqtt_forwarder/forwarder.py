import sys
from os import environ

import paho.mqtt.client as mqtt

LOCAL_MQTT_HOST = "mosquitto-service"
LOCAL_MQTT_PORT = 1883
LOCAL_MQTT_TOPIC = "camera_topic"

REMOTE_MQTT_HOST = environ.get("AWS_IP")
REMOTE_MQTT_PORT = 1883
REMOTE_MQTT_TOPIC = "cloud_topic"


def on_connect_local(client, userdata, flags, rc):
    print("Connected to local broker with rc: " + str(rc))
    client.subscribe(LOCAL_MQTT_TOPIC)


def on_connect_remote(client, userdata, flags, rc):
    print("Connected to remote broker with rc: " + str(rc))
    client.subscribe(REMOTE_MQTT_TOPIC)


remote_mqttclient = mqtt.Client("aws-broker")
remote_mqttclient.on_connect = on_connect_remote
remote_mqttclient.connect(REMOTE_MQTT_HOST, REMOTE_MQTT_PORT, 60)


def on_message(client, userdata, msg):
    try:
        print("Message received: ", str(msg.payload.decode("ISO-8859-1")))

        msg = msg.payload
        remote_mqttclient.publish(REMOTE_MQTT_TOPIC, payload=msg, qos=0, retain=False)
    except:
        print("Unexpected error: ", sys.exc_info()[0])


local_mqttclient = mqtt.Client()
local_mqttclient.on_connect = on_connect_local
local_mqttclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)
local_mqttclient.on_message = on_message

local_mqttclient.loop_forever()
