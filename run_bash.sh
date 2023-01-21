#! bin/bash

# Include all docker commands used

apt-get update

# Install paho-mqtt
# Install opencv

# Install Kubernetes (K3)
sudo apt update
sudo apt install -y curl
	
mkdir $HOME/.kube/
curl -sfL https://get.k3s.io | sh -s - --docker --write-kubeconfig-mode 644 --write-kubeconfig $HOME/.kube/config
#sudo systemctl disable k3s
sudo systemctl start k3s
sudo systemctl stop k3s

# Install MQTT
sudo apt install -y mosquitto-clients
sudo apt install -y mosquitto

cd /camera
docker build -t hsiungc/camera:v1 .
docker run -it --rm --device /dev/video0 --network host -e DISPLAY=$DISPLAY camera:latest

cd ../mqtt_broker
docker build -t hsiungc/mosquitto:v2 .
docker build -t hsiungc/mqtt_broker:v1 .
docker run

cd ../mqtt_logger
docker build -t hsiungc/mqtt_logger:v1

# Apply YAMLs
kubectl apply -f /k8s_yaml

