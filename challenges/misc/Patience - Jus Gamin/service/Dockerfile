FROM debian:stable

COPY pain.py .
COPY ynetd .

RUN chmod +x ynetd
RUN apt update && apt install python3 -y

CMD ./ynetd -p 1337 "python3 pain.py"