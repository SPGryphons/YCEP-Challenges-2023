# Use a base image
FROM ubuntu:latest
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y openssh-server
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y openssh-server
RUN echo "root:WJj5gmdmDXzHe27^xk%P" | chpasswd
RUN sed -i 's/#Port 22/Port 22000/' /etc/ssh/sshd_config
RUN sed -i 's/PermitRootLogin yes/PermitRootLogin no/' /etc/ssh/sshd_config
RUN sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config
RUN useradd -m -s /bin/bash ycep_user
RUN echo "ycep_user:ycep_user" | chpasswd

COPY ./what /home/ycep_user/what
RUN chmod 555 /home/ycep_user/what
COPY chall.txt /home/ycep_user/chal.txt

RUN mkdir /run/sshd

EXPOSE 22000

CMD ["/usr/sbin/sshd", "-D"]