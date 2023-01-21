# 251-hsiungc-hw1

Edge VM:
	- Use Alpine Linux as base OS for MQTT containers
	[x] Install MQTT broker on Edge VM --> "apt install mosquitto"
		- Face detector should send to this broker first (local broker)
	- Install local listener
		- output to log that received a face message (standard out)
	Application:
	Face detection —> OpenCV
		- scan video frames coming from camera for faces
		- cut out faces from frame and send via binary message for each face
		- Use MQTT
		- Use Ubuntu as base for container

- Need another component that receives messages from local broker and send them to cloud (MQTT broker)???

AWS VM:
	- Lightweight = micro

	Containers:
		- MQTT broker in Docker container
			- faces sent as binary messages

- Need second component that receives messages and saves to S3 (LOOK AT BOTO)

s3 Object storage
	- Use both to receive and save images