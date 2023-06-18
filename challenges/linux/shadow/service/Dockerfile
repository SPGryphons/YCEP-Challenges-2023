FROM ubuntu:latest

RUN apt-get update && apt-get install -y openssh-server

RUN useradd -m -s /bin/bash pwn_me
RUN useradd -m -s /bin/bash ycep_user

RUN echo 'pwn_me:lucky13' | chpasswd
RUN echo 'ycep_user:ycep_user' | chpasswd

COPY flag.txt /home/pwn_me/
COPY message.txt /home/ycep_user/

RUN chown -R pwn_me:pwn_me /home/pwn_me
RUN chown -R ycep_user:ycep_user /home/ycep_user

# Make /etc/shadow world-readable & prevent griefing
RUN chmod o+r /etc/shadow
RUN chmod -R 500 /home/pwn_me
RUN chmod -R 500 /home/ycep_user

# ssh
RUN mkdir /var/run/sshd
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin no/' /etc/ssh/sshd_config
EXPOSE 22
CMD service ssh start && su ycep_user
