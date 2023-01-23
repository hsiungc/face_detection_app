FROM alpine:latest

RUN apk update
RUN apk --no-cache add mosquitto mosquitto-clients

EXPOSE 1883

RUN echo "allow_anonymous true" > /etc/mosquitto/mosquitto.conf
RUN echo "listener 1883 0.0.0.0" >> /etc/mosquitto/mosquitto.conf

CMD ["mosquitto","-c","/etc/mosquitto/mosquitto.conf"]
