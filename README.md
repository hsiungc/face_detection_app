<h1>Face Detection Edge Deployment</h1>

The purpose of this project is to deploy a face detection application on an NVIDIA Jetson Nano device, which will stream facial images to an AWS EC2 instance in the cloud and store them into an object storage.

MQTT is the messaging service for this deployment. The face detection app (camera) will publish image frames as bytes to the MQTT broker, which in turn pushes the messages to the subscribed logger and the forwarder in the edge VM. The forwarder sends the messages to the broker and the image processor in the cloud. After the processor receives the messages, it automatically converts the bytes into images that are pushed into an S3 bucket.

## Building the Face Detection Application
Once Ubuntu is up and running on a VM, perform an initial setup of the workspace. Docker, K3s, Mosquitto (MQTT), and the AWS CLI are required for this project. Workspace setup commands are found in the setup.sh file (installing K3s and other libraries/packages, setting up the EC2 instance)

To kick off, the following components should be built in the edge VM; first in Docker, then in Kubernetes. See the component.sh script for the commands.

Edge VM
- MQTT Broker
- MQTT Logger
- Camera
- MQTT Forwarder*

***The forwarder deployment requires the AWS IP and AWS MQTT broker NodePort environment variables to be updated manually every time the EC2 instance is spun up.**

Once all components are built and deployed, additional containers should be set up in the EC2 instance (upgraded to t2.medium). Another MQTT broker and the image processor are created here. If K3s is chosen for the orchestration and networking, it needs to be installed into the VM. The YAML file text are copied and pasted, and the containers are pulled from DockerHub.

Cloud VM
- MQTT Broker
- Image Processor

Make sure an S3 bucket is already configured (in this case, the bucket is '251-bucket'). The code running the image processor automatically sends the images for storage in the S3 bucket.

An IAM role for access to S3 needs to be configured and mounted to the EC2 instance. The access key and secret key are called as environment variables into the image processor deployment YAML. This will allow the processor to push the decoded images into S3. For purposes of security, both keys are not included in the GitHub repository. 

The S3 bucket can be accessed here: ~~https://s3.console.aws.amazon.com/s3/buckets/251-bucket~~

## Running the Face Detection Application
The app should run automatically once the camera container is deployed. Be ready to smile and include as many people as needed in the camera frame.

## Future Goals
There was much learning involved in building this application. In the future, I will look into the following for self-exploration:

1. Smaller containers (i.e.; multistage builds)
2. InitContainers and healthchecks in Kubernetes - currently, some of the containers will crashloop until the image finishes setting up.
3. IAM and security (i.e.; least privilege)
4. Other messaging services
5. Ingressing instead of NodePorts