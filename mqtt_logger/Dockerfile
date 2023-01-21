FROM alpine:3.17

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apk update

RUN apk add --no-cache python3 py3-pip

RUN pip3 install paho-mqtt

COPY logger.py .

CMD python3 logger.py
