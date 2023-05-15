FROM debian:stable

COPY app/ .

RUN chmod +x ynetd
RUN apt update && apt install python3 -y

CMD ./ynetd -p 1337 "python3 main.py"