FROM ubuntu:latest
WORKDIR /code
COPY . /code
RUN apt-get update -y && apt-get upgrade -y
CMD ./hotel
EXPOSE 3000