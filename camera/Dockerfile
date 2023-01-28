ARG APP_DIR=/app

FROM ubuntu:18.04 AS build
ARG APP_DIR

ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y \
	build-essential \
	cmake \
    python3 \
    python3-dev \
    python3-venv \
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

RUN apt-get autoclean && apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
    
WORKDIR ${APP_DIR}

RUN python3 -m venv /venv
ENV PATH /venv/bin:$PATH

RUN pip3 install numpy paho-mqtt

RUN git clone https://github.com/opencv/opencv.git
RUN git clone https://github.com/opencv/opencv_contrib.git

RUN cd opencv && git checkout 3.4.1 && cd ..
RUN cd opencv_contrib && git checkout 3.4.1 && cd ..

WORKDIR ${APP_DIR}/opencv

ENV SITE_PACKAGES ${APP_DIR}/venv/lib/python3.10/site-packages
ENV EXTRA_MODULES ${APP_DIR}/opencv_contrib/modules

RUN mkdir ./build && \
	cd build && \
	cmake -D CMAKE_BUILD_TYPE=RELEASE \
	-D INSTALL_PYTHON_EXAMPLES=ON \
	-D INSTALL_C_EXAMPLES=OFF \
	-D PYTHON_EXECUTABLE=$(which python3) \
	-D BUILD_OPENCV_PYTHON2=OFF \
	-D CMAKE_INSTALL_PREFIX=$(python3 -c "import sys; print(sys.prefix)") \
	-D PYTHON3_EXECUTABLE=$(which python3) \
	-D PYTHON3_INCLUDE_DIR=$(python3 -c "from distutils.sysconfig import get_python_inc; print(get_python_inc())") \
	-D PYTHON3_PACKAGES_PATH=$(python3 -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())") \
	-D OPENCV_PYTHON3_INSTALL_PATH=$SITE_PACKAGES \
    -D OPENCV_EXTRA_MODULES_PATH=$EXTRA_MODULES \
	-D CMAKE_INSTALL_PREFIX=/build \
    	-D WITH_GSTREAMER=ON \
	-D BUILD_EXAMPLES=ON .. && \
	make -j$(nproc) && \
	make install


FROM ubuntu:18.04 AS runtime
ARG APP_DIR

RUN apt-get update && apt-get install -y \
	python3 \
    python3-dev \
	python3-venv \
    python3-pip && \
	rm -rf /var/lib/apt/lists/*
	
WORKDIR ${APP_DIR}

COPY --from=build /venv /venv
COPY --from=build /build /build

ENV PATH /venv/bin:$PATH

RUN ldconfig /opencv/build

COPY camera.py haarcascade_frontalface_default.xml ./

CMD ["python3", "camera.py"]