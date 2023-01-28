FROM ubuntu:latest

ENV PYTHONUNBUFFERED=1
ENV TZ=US/Pacific

WORKDIR /app

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update && \
    apt install -y python3 python3-dev python3-pip \
    python3-opencv vim-tiny libopencv-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install Cython
RUN pip3 install numpy paho-mqtt

COPY camera.py haarcascade_frontalface_default.xml ./

CMD ["python3", "camera.py"]
