# syntax=docker/dockerfile:1
FROM ubuntu:latest
WORKDIR /code
COPY . /code
RUN apt-get update -y && apt-get upgrade -y
RUN chmod +x hazbin
CMD ./hazbin
EXPOSE 3000