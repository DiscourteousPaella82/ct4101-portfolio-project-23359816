# Building image processing service
FROM python:3.14.8-slim-bookworm AS application-builder

RUN python3.14 -m venv /home/user/venv

ENV PATH="/home/user/venv/bin:$PATH"

RUN mkdir /home/user/app
WORKDIR /home/user/app
RUN mkdir ./output

ADD ./requirements.txt .

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
RUN pip3 install --no-cache-dir wheel
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

# Image processing
FROM application-builder AS image-processor-runner 

WORKDIR /home/user/app/image-processing-service/src/image-processing

ENV PYTHONUNBUFFERED=1
ENV VIRTUAL_ENV=/home/user/venv

ARG TOTAL_IMAGES_COUNT
ENV IMAGES_PATH=/home/user/app/assets
ENV TOTAL_IMAGES_COUNT=${TOTAL_IMAGES_COUNT}

RUN python3 __init__.py -v -o /home/user/app/output

# Image processing
FROM image-processor-runner AS image-classifier-runner 

WORKDIR /home/user/app/image-classification-service/src/Image-classification

ARG DATA_PATH=/home/user/app/output/data.json
ENV DATA_PATH=${DATA_PATH}

RUN mkdir /home/user/app/output/graphs

RUN python3 __init__.py -v -p -s -o /home/user/app/output/graphs