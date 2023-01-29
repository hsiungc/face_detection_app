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

# Main packages
# Install MQTT (for testing)
sudo apt install -y mosquitto-clients
sudo apt install -y mosquitto

# Install paho-mqtt (for testing)
pip3 install paho-mqtt

# Install opencv (for testing)
pip3 install python3-opencv


# AWS CLI
# Network ports from Edge to AWS
aws ec2 authorize-security-group-ingress --group-id sg-02533bccf0f3de13d --protocol tcp --port 1883 --cidr 0.0.0.0/0
aws ec2 authorize-security-group-ingress --group-id sg-02533bccf0f3de13d --protocol tcp --port 30145 --cidr 0.0.0.0/0 #NodePort port

# SSH into EC2 instance
ssh-add -K "your_keypair.pem" 
ssh-add -L

ssh -A ubuntu@ec2-3-83-245-179.compute-1.amazonaws.com 

sudo su