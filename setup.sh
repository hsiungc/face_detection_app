#! bin/bash

# System setup
apt-get update

# Install Kubernetes (K3s)
sudo apt update
sudo apt install -y curl
	
mkdir $HOME/.kube/
curl -sfL https://get.k3s.io | sh -s - --docker --write-kubeconfig-mode 644 --write-kubeconfig $HOME/.kube/config

#Set up K3s
sudo systemctl disable k3s
sudo systemctl start k3s
sudo systemctl stop k3s

# Install MQTT
sudo apt install -y mosquitto-clients
sudo apt install -y mosquitto

# Install paho-mqtt
pip3 install paho-mqtt

# Install opencv