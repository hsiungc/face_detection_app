import logging
import os
import sys

import boto3
import paho.mqtt.client as mqtt
from botocore.exceptions import ClientError

BUCKET = "251-bucket"
S3_CLIENT = boto3.client("s3")


def upload_file(file_name, bucket, obj_name=None):
    if obj_name is None:
        obj_name = os.path.basename(file_name)

    try:
        response = S3_CLIENT.upload_file(file_name, bucket, obj_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True


LOCAL_MQTT_HOST = "mosquitto-service"
LOCAL_MQTT_PORT = 1883
LOCAL_MQTT_TOPIC = "cloud_topic"


def on_connect_local(client, userdata, flags, rc):
    print("Connected to local broker with rc: " + str(rc))
    client.subscribe(LOCAL_MQTT_TOPIC)


def on_message(client, userdata, msg):
    try:
        print("Message received: ", str(msg.payload.decode("ISO-8859-1")))
        upload_file(msg, BUCKET)

    except:
        print("Unexpected error:", sys.exc_info()[0])


local_mqttclient = mqtt.Client()
local_mqttclient.on_connect = on_connect_local
local_mqttclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)
local_mqttclient.on_message = on_message


local_mqttclient.loop_forever()
