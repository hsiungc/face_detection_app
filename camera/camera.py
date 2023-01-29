import cv2
import numpy as np
import paho.mqtt.client as mqtt

LOCAL_MQTT_HOST = "mosquitto-service"
LOCAL_MQTT_PORT = 1883
LOCAL_MQTT_TOPIC = "camera_topic"


def on_connect_local(client, userdata, flags, rc):
    print("Connected to local broker with rc" + str(rc))


local_mqttclient = mqtt.Client()
local_mqttclient.on_connect = on_connect_local
local_mqttclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0, cv2.CAP_V4L2)

while True:
    # Read and apply procedure to every frame
    ret, frame = cap.read()
    	
    # Convert image color to greyscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:

        # Draw the rectangle
        cv2.rectangle(gray, (x, y), (x + w, y + h), (0, 0, 0), 3)
        roi = gray[y : y + h, x : x + w]

        # Encode the image
        png = cv2.imencode(".png", roi)[1]
        np_png = np.array(png)
        msg = np_png.tobytes()

        local_mqttclient.publish(LOCAL_MQTT_TOPIC, msg)
        
        # Show image in window
        # cv2.imshow("frame", gray)
    
        # End if 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

cap.release()
cv2.destroyAllWindows()
