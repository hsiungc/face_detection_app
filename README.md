# 251-hsiungc-hw2
The purpose of HW2 is to deploy a face detection python script on an edge VM, which will store facial images through an AWS EC2 instance into object storage.

# Building the Application
After running Ubuntu 18.04 through a VM (VMware Fusion), clone the repo and perform an initial setup of the workspace. Docker, K3s, Mosquitto (MQTT), and the AWS CLI are required for this homework. Workspace setup commands are found in the setup.sh file (installing K3s, Mosquitto (MQTT))

To kickoff the homework, the following components should be built in the following order:

	1. MQTT Broker
	2. MQTT Logger
	4. Camera
	3. MQTT Forwarder

Once all components have been deployed, additional containers should be set up in an EC2 instance.

# Running the Application


#### Kubernetes Objects:

#### Docker Images: