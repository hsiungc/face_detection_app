# 251-hsiungc-hw2
The purpose of HW2 is to deploy a face detection python script on an edge VM, which will store facial images through an AWS EC2 instance into object storage.

MQTT is the messaging service of choice for this homework. The face detection app (camera) will publish image frames as bytes to the MQTT broker, which in turn pushes the messages to the subscribed logger and the forwarder in the edge VM. The forwarder sends the messages to the broker and the image processor in the cloud. After the processor receives the messages, it automatically converts the bytes into images that are pushed into an S3 bucket.

# Building the Face Detection Application
Once Ubuntu is up and running on a VM, perform an initial setup of the workspace. Docker, K3s, Mosquitto (MQTT), and the AWS CLI are required for this homework. Workspace setup commands are found in the setup.sh file (installing K3s and other libraries/packages, setuping up the EC2 instance)

To kickoff the homework, the following components should be built in the edge VM; first in Docker, then in Kubernetes. See the component.sh script for the commands.

Edge VM
	1. MQTT Broker
	2. MQTT Logger
	4. Camera
	3. MQTT Forwarder*

*The forwarder deployment requires the AWS IP and AWS MQTT broker NodePort environment variables to be updated manually everytime the instance is spun up.

Once all components are built and deployed, additional containers should be set up in the EC2 instance (upgraded to t2.medium). Another MQTT broker and the image processor are created here. If K3s is chosen for the orchestration and networking, it needs to be installed into the VM. The yaml file text are copied and pasted, and the containers are pulled from DockerHub.

Cloud VM
	1. MQTT Broker
	2. Image Processor

Make sure an S3 bucket is already configured (in this case, the bucket is '251-bucket'). The code running the image processor automatically sends the images for storage in the S3 bucket.

# Running the Face Detection Application
The app should run automatically once the camera container is deployed. Be ready to smile and include as many people as you want in the camera frame.