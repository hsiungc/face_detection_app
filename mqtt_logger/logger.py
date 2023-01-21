import paho.mqtt.client as mqtt
import sys

LOCAL_MQTT_HOST = "mosquitto-service"
LOCAL_MQTT_PORT = 1883
LOCAL_MQTT_TOPIC = "camera_topic"

def on_connect_local(client, userdata, flags, rc):
    print("Connected to message logger on rc: " + str(rc))
    client.subscribe(LOCAL_MQTT_TOPIC)

def on_message(client, userdata, msg):
    try:
        print("Message received: ", str(msg.payload.decode("ISO-8859-1")))

    except:
        print("Unexpected error: ", sys.exc_info()[0])
    

local_mqttclient = mqtt.Client()
local_mqttclient.on_connect = on_connect_local
local_mqttclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)
local_mqttclient.on_message = on_message

local_mqttclient.loop_forever()
