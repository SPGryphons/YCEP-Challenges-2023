FROM ubuntu:latest
WORKDIR /free-wifi
COPY wifi.c .
COPY flag.txt .
COPY ynetd .
EXPOSE 3006
RUN apt-get update && apt-get install -y gcc
RUN gcc wifi.c -o wifi -fno-stack-protector -z execstack -no-pie
CMD ./ynetd -p 3006 ./wifi