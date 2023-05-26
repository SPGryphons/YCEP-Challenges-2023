FROM ubuntu:latest
WORKDIR /code
COPY . /code
RUN apt-get update -y && apt-get upgrade -y
RUN chmod +x hotel
CMD ./hotel
EXPOSE 3000