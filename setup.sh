#! bin/bash

# System setup
apt-get update

sudo su

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


ssh-add -K "your_keypair.pem" 
ssh-add -L


ssh -A ubuntu@ec2-3-83-245-179.compute-1.amazonaws.com 

sudo su

aws ec2 authorize-security-group-ingress --group-id sg-02533bccf0f3de13d --protocol tcp --port 1883 --cidr 0.0.0.0/0
aws ec2 authorize-security-group-ingress --group-id sg-02533bccf0f3de13d --protocol tcp --port 30145 --cidr 0.0.0.0/0