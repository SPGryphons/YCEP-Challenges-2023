FROM ubuntu:latest

ENV user=pythonlover

RUN apt-get update -y
RUN apt-get install -y python2
RUN useradd -m $user
RUN mkdir -p /home/$user/flag

COPY ./main.py /home/$user/
COPY ./flag/flag.txt /home/$user/flag/

RUN chown root:$user /home/$user/main.py
RUN chmod 440 /home/$user/main.py
RUN chown root:$user /home/$user/flag
RUN chmod 444 /home/$user/flag
RUN chmod +x /home/$user/flag

USER pythonlover

WORKDIR /home/pythonlover

EXPOSE 49760

CMD ["python2", "/home/pythonlover/main.py"]