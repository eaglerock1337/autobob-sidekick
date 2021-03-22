FROM python:3.8-slim

RUN apt update && apt install -y binutils

WORKDIR /code
COPY . .
