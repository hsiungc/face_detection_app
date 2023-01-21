import paho.mqtt.client as mqtt

LOCAL_MQTT_HOST=""
LOCAL_MQTT_PORT=""
LOCAL_MQTT_TOPIC=""
REMOTE_MQTT_TOPIC=""

def on_connect_local(client, userdata, flags, rc):
    print("Connected to local broker with rc: " + str(rc))
    client.subscribe(LOCAL_MQTT_TOPIC)

def on_message(client, userdata, msg):
    try:
        print("Message received: ", str(msg.payload.decode("utf-8")))

        msg = msg.payload
        remote_mqttclient.publish(REMOTE_MQTT_TOPIC, payload=msg, qos=0, retain=False)
    except:
        print("Unexpected error: ", sys.exc_info()[0])

local_mqttclient = mqtt.Client()
local_mqttclient.on_connect = on_connect_local
local_mqttclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)
local_mqttclient.on_message = on_message

local_mqttclient.loop_forever()