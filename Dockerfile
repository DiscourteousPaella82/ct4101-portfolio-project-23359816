FROM python:3.14.8-slim-bookworm AS build

RUN python3.14 -m venv /home/user/venv

ENV PATH="/home/myuser/venv/bin:$PATH"

RUN mkdir /home/user/app
WORKDIR /home/user/app

COPY . .

WORKDIR /home/user/app/image-processing-service

RUN pip3 install --no-cache-dir wheel
RUN pip3 install --no-cache-dir -r requirements.txt