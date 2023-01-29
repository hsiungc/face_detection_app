#! bin/bash

# MQTT Broker
docker build -t hsiungc/mosquitto:v1 .
docker push hsiungc/mosquitto:v1

kubectl apply -f mosquittoDeployment.yaml
kubectl apply -f mosquittoService.yaml


# MQTT Logger
docker build -t hsiungc/mqtt_logger:v1 .
docker push hsiungc/mqtt_logger:v1

kubectl apply -f loggerDeployment.yaml
kubectl apply -f loggerService.yaml


# MQTT Forwarder
docker build -t hsiungc/mqtt_forwarder:v1
docker push hsiungc/mqtt_forwarder:v1

kubectl apply -f forwarderDeployment.yaml
kubectl apply -f forwarderService.yaml


# Camera Deployment
docker build -t hsiungc/camera:v2 .
docker run -it --rm --device /dev/video0 --network host -e DISPLAY=$DISPLAY hsiungc/camera:v2 # Test with Docker
docker push hsiungc/camera:v2

kubectl apply -f cameraDeployment.yaml
kubectl apply -f cameraDeployment.yaml


# Image Processor
docker build -t hsiungc/mqtt_processor:v1
docker push hsiungc/mqtt_processor:v1

kubectl apply -f processorDeployment.yaml
kubectl apply -f processorrService.yaml
