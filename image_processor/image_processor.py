import io
from datetime import datetime
from os import environ

import boto3
import numpy as np
import paho.mqtt.client as mqtt

BUCKET = "251-bucket"
S3_CLIENT = boto3.client(
    "s3",
    aws_access_key_id=environ.get("ACCESS_KEY"),
    aws_secret_access_key=environ.get("SECRET_KEY"),
)

LOCAL_MQTT_HOST = "mosquitto-service"
LOCAL_MQTT_PORT = 1883
LOCAL_MQTT_TOPIC = "camera_topic"


def on_connect_local(client, userdata, flags, rc):
    print("Connected to local broker with rc: " + str(rc))
    client.subscribe(LOCAL_MQTT_TOPIC)


def on_message(client, userdata, msg):
    try:
        print("Message received.")

        msg = msg.payload
        decode = np.frombuffer(msg, dtype="uint8")
        img = io.BytesIO(decode)

        now = datetime.now()
        dt_string = now.strftime("%Y-%m-%d-%H-%M-%S")
        file = "face-" + dt_string + ".png"

        S3_CLIENT.put_object(Key=file, Bucket=BUCKET, Body=img, ContentType="image/png")
        print("Pushed to S3")

    except:
        print("Unexpected error.")


local_mqttclient = mqtt.Client()
local_mqttclient.on_connect = on_connect_local
local_mqttclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)
local_mqttclient.on_message = on_message


local_mqttclient.loop_forever()
