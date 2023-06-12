FROM ubuntu:latest

# Install necessary packages
RUN apt-get update && apt-get install -y openssh-server

# Create pwn_me user
RUN useradd -m -s /bin/bash pwn_me

# Create ycep_user user
RUN useradd -m -s /bin/bash ycep_user

# Change password for pwn_me
RUN echo 'pwn_me:secret_password_12345' | chpasswd

# Change password for ycep_user
RUN echo 'ycep_user:ycep_user' | chpasswd

# Make /etc/shadow world-readable & prevent griefing
RUN chmod o+r /etc/shadow
COPY flag.txt /home/pwn_me/Desktop/
RUN chmod 555 /home/pwn_me /home/ycep_user

# Set up SSH server
RUN mkdir /var/run/sshd
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin no/' /etc/ssh/sshd_config

# Start SSH server on port 22
EXPOSE 22

# Start a shell as ycep_user and run SSH server
CMD service ssh start && su ycep_user
