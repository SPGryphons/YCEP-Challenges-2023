FROM ubuntu:latest

# Install necessary packages
RUN apt-get update && apt-get install -y netcat

# Create pwn_me user
RUN useradd -m -s /bin/bash pwn_me

# Create ycep_user user
RUN useradd -m -s /bin/bash ycep_user

# change pw for pwn_me
RUN echo 'pwn_me:secret_password_12345' | chpasswd

# change pw for ycep_user
RUN echo 'ycep_user:ycep_user' | chpasswd

# Make /etc/shadow world-readable & prevent griefing 
RUN chmod o+r /etc/shadow
COPY flag.txt /home/pwn_me/Desktop/
RUN chmod 555 /home/pwn_me /home/ycep_user

# Start a shell as ycep_user
CMD su ycep_user
CMD ./ynetd -p 1337 /bin/bash
