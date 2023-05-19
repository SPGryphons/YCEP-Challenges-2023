FROM ubuntu:latest

RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install python3.10 -y
RUN apt-get install ncat -y
WORKDIR /home/ctf

COPY . /home/ctf
RUN rm flag.txt
WORKDIR /home

COPY flag.txt /home

WORKDIR /home/ctf

EXPOSE 8000

CMD ncat -lvnp 8000 -k -e "/bin/python3.10 main.py"