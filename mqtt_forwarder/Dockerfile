FROM alpine:latest

ENV PYTHONUNBUFFERED=1

RUN apk update

RUN apk --no-cache add python3 py3-pip

RUN python3 -m ensurepip

RUN pip3 install --no-cache --upgrade pip setuptools
RUN pip3 install paho-mqtt

WORKDIR /app

COPY forwarder.py .

CMD python3 forwarder.py

