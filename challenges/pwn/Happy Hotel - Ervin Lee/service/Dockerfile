FROM ubuntu:latest
WORKDIR /code
COPY . /code
RUN apt-get update -y && apt-get upgrade -y
RUN chmod +x ynetd
RUN chmod +x hotel
CMD ./ynetd -p 3001 ./hotel
EXPOSE 3001