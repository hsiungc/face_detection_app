FROM alpine:latest

ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip3 install paho-mqtt

WORKDIR /app

COPY logger.py .

CMD python3 logger.py