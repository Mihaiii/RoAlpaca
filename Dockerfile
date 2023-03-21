FROM pytorch/pytorch:1.13.1-cuda11.6-cudnn8-runtime

COPY . /app
WORKDIR /app

RUN apt update && apt upgrade -y
RUN apt install -y git

RUN pip install -r requirements.txt