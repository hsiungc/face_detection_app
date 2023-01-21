FROM ubuntu:latest

ENV PYTHONUNBUFFERED=1

WORKDIR /src

RUN apt-get update && \
    apt install -y python3 python3-dev python3-pip \
    python3-opencv vim-tiny libopencv-dev

RUN pip3-install Cython
RUN pip3 install numpy paho-mqtt

COPY /src .

CMD ["python3 cam.py"]