# Use a base image
FROM ubuntu:latest
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y openssh-server
RUN echo "root:dPTB^WXd4tavVsMP" | chpasswd
RUN sed -i 's/#Port 22/Port 22000/' /etc/ssh/sshd_config
RUN sed -i 's/PermitRootLogin yes/PermitRootLogin no/' /etc/ssh/sshd_config
RUN sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config
RUN useradd -m -s /bin/bash ycep_user
RUN echo "ycep_user:ycep_user" | chpasswd

COPY ./haystack /home/ycep_user/haystack
COPY challenge.txt /home/ycep_user/challenge.txt
RUN chmod 555 /home/ycep_user/haystack

# Create the /run/sshd directory
RUN mkdir /run/sshd

# Expose SSH port 22000
EXPOSE 22000

# Start the OpenSSH server
CMD ["/usr/sbin/sshd", "-D"]
