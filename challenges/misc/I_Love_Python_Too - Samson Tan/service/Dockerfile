FROM ubuntu:latest

ENV user=pythonlover

RUN apt-get update -y
RUN apt-get install -y python2 netcat
RUN useradd -m $user
RUN mkdir -p /home/$user/flag

COPY ./main.py /home/$user/
COPY ./flag/flag.txt /home/$user/flag/
COPY ./ynetd /home/$user/

RUN chown root:$user /home/$user/main.py
RUN chmod 440 /home/$user/main.py
RUN chown root:$user /home/$user/flag
RUN chmod 444 /home/$user/flag
RUN chmod +x /home/$user/flag
RUN chmod +x /home/$user/ynetd

USER pythonlover

WORKDIR /home/pythonlover

EXPOSE 1337

# ha using ynetd again, what are ya gonna do about it?

CMD ["/home/pythonlover/ynetd", "-p", "1337", "python2 -u /home/pythonlover/main.py"]
