#! bin/bash

# Include all docker commands used

# Double check arm64


# Apply Docker networking
docker network create --driver bridge 251_network
docker network ls
docker container attach mqtt_logger
ping -c 2 mosquitto


# MQTT Broker
cd mqtt_broker/
docker build --network 251_network --platform linux/arm64 -t hsiungc/mosquitto:v1 .
docker run hsiungc/mosquitto:v1
docker push hsiungc/mosquitto:v1


# MQTT Logger
cd ../mqtt_logger
docker build --network 251_network --platform linux/arm64 -t hsiungc/mqtt_logger:v1 .
docker run hsiungc/mqtt_logger:v1
docker push hsiungc/mqtt_logger:v1


# Camera Deployment
cd ../camera
docker build --network 251_network --platform linux/arm64 -t hsiungc/camera:v1 .
docker run -it --rm --device /dev/video0 --network host -e DISPLAY=$DISPLAY camera:latest
docker push hsiungc/camera:v1

# Apply camera


# MQTT Forwarder
cd ../mqtt_forwarder
docker build --network 251_network --platform linux/arm64 -t hsiungc/mqtt_forwarder:v1
docker run hsiungc/mqtt_forwarder:v1
docker push hsiungc/mqtt_forwarder:v1




# Apply YAMLs
kubectl apply -f /k8s_yaml

# Check MQTT logger
kubectl get pods # Get pod name
kubectl logs -f # <logger pod name>
