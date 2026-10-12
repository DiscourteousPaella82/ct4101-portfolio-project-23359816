# Building image processing service
FROM python:3.14.8-slim-bookworm AS image-processor-builder

RUN python3.14 -m venv /home/user/venv

ENV PATH="/home/myuser/venv/bin:$PATH"

RUN mkdir /home/user/app
WORKDIR /home/user/app

COPY . .

WORKDIR /home/user/app/image-processing-service

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
RUN pip3 install --no-cache-dir wheel
RUN pip3 install --no-cache-dir -r requirements.txt

RUN mkdir /home/user/assets
WORKDIR /home/user/assets
COPY ./assets .

# Image processing
FROM image-processor-builder AS image-processor-runner 

ENV PATH="/home/myuser/venv/bin:$PATH"

WORKDIR /home/user/app/image-processing-service/src/image-processing

ENV PYTHONUNBUFFERED=1
ENV VIRTUAL_ENV=/home/user/venv

ENV IMAGES_PATH="/home/user/assets"
ENV TOTAL_IMAGE_COUNT=$TOTAL_IMAGE_COUNT

RUN [ "python3", "__init__.py" ]