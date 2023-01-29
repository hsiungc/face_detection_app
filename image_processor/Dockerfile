FROM ubuntu:latest

ENV DEBIAN_FRONTEND noninteractive
ENV PYTHONUNBUFFERED=1
ENV TZ=US/Pacific

WORKDIR /app

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

WORKDIR /app

RUN apt-get update && \
    apt install -y python3 python3-dev python3-pip vim-tiny \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install Cython
RUN pip3 install numpy paho-mqtt boto3

COPY image_processor.py .

CMD python3 image_processor.py
