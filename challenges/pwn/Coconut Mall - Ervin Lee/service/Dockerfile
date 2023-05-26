FROM ubuntu:latest

WORKDIR /coconut

COPY coconut .
COPY flag.txt .
COPY ynetd .
RUN chmod +x coconut
RUN chmod +x ynetd
EXPOSE 3002

CMD ./ynetd -p 3002 ./coconut
# Test comment