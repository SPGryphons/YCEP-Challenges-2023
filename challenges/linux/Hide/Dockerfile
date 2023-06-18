# Use a base image
FROM ubuntu:latest

# Update package lists
RUN apt-get update && apt-get upgrade -y

# Install OpenSSH server
RUN apt-get install -y openssh-server

# Set the root password to 'dPTB^WXd4tavVsMP'
RUN echo "root:dPTB^WXd4tavVsMP" | chpasswd

# Set the SSH port to 22000
RUN sed -i 's/#Port 22/Port 22000/' /etc/ssh/sshd_config

# Disable root login
RUN sed -i 's/PermitRootLogin yes/PermitRootLogin no/' /etc/ssh/sshd_config

# Enable password authentication
RUN sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config

# Create a restricted bash (rbash) user
RUN useradd -m -s /bin/rbash user

# Set the user password to 'qwerty'
RUN echo "user:qwerty" | chpasswd

# Set file permission on flag.txt to o=r
RUN touch /home/user/flag.txt && chown root:root /home/user/flag.txt && chmod o=r /home/user/flag.txt
RUN echo "YCEP2023{Try_H4rd3r}" > /home/user/flag.txt

RUN touch /home/user/.flag.txt && chown root:root /home/user/.flag.txt && chmod o=r /home/user/.flag.txt
RUN echo "YCEP2023{L1nux_Wi11_4lw4y5_B3_W1th_Y0u}" > /home/user/.flag.txt

# Create the /run/sshd directory
RUN mkdir /run/sshd

# Expose SSH port 22000
EXPOSE 22000

# Start the OpenSSH server
CMD ["/usr/sbin/sshd", "-D"]
