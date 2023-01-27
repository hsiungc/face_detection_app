FROM ubuntu:latest AS build

ENV PYTHONUNBUFFERED=1

RUN apt-get update 
RUN apt-get upgrade -y

RUN \
	apt-get install -y \
    build-essential \
    cmake \
    python3 \
    python3-dev \
    python3-pip \
    gcc \
    git \
    vim-tiny \
	libgstreamer1.0-0 \
	gstreamer1.0-plugins-base \
	gstreamer1.0-plugins-good \
	gstreamer1.0-plugins-bad \
	gstreamer1.0-plugins-ugly \
	gstreamer1.0-libav \
	gstreamer1.0-doc \
	gstreamer1.0-tools \
	libgstreamer1.0-dev \
	libgstreamer-plugins-base1.0-dev

RUN git clone https://github.com/opencv/opencv.git

RUN apt-get autoclean && apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN \
	cd opencv && \
	git checkout 4.5.4 && \
	git submodule update --recursive --init && \
	mkdir /prefix && \
	cd /prefix && \
	cmake -D CMAKE_BUILD_TYPE=RELEASE \
    -D PYTHON_EXECUTABLE=$(which python3) \
	-D PYTHON3_EXECUTABLE=$(which python3) \
	-D PYTHON3_INCLUDE_DIR=$(python3 -c "from distutils.sysconfig import get_python_inc; print(get_python_inc())") \
	-D PYTHON3_PACKAGES_PATH=$(python3 -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())") \
	-D CMAKE_INSTALL_PREFIX=/prefix \
    -D WITH_GSTREAMER=ON \
	-D BUILD_EXAMPLES=ON .. && \
	make -j$(nproc) && \
	make install


FROM ubuntu:latest AS runtime

COPY --from=build /prefix /prefix

RUN ldconfig /prefix

WORKDIR /app

RUN pip3 install numpy paho-mqtt

COPY camera.py haarcascade_frontalface_default.xml ./

CMD ["python3", "camera.py"]
