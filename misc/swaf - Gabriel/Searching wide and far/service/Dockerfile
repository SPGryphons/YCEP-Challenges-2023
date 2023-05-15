FROM debian:stable

RUN apt-get update && apt-get install -y gcc

COPY flag.txt .
COPY looking.c .
COPY ynetd .

RUN gcc -o look looking.c

RUN chmod +x look
RUN chmod +x ynetd

CMD ./ynetd -p 1337 ./look
