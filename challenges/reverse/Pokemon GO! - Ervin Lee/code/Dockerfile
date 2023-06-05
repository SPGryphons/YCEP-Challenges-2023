# syntax=docker/dockerfile:1
FROM ubuntu:latest
WORKDIR /pokemon
COPY pokemon.go /etc
COPY something.txt /tmp
COPY ynetd .
RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install golang -y
RUN go build /etc/pokemon.go
RUN chmod +x pokemon
RUN chmod +x ynetd
EXPOSE 3001
CMD ./ynetd -p 3001 /bin/rbash
