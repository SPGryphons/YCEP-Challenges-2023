# syntax=docker/dockerfile:1
FROM ubuntu:latest
WORKDIR /code
COPY . /code
RUN apt-get update -y && apt-get upgrade -y
RUN chmod +x ynetd
RUN chmod +x hazbin
CMD ./ynetd -p 3000 ./hazbin
EXPOSE 3000