# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory contents into the container at /app
COPY app.py /app
COPY index.html /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir flask

# Make port 1337 available to the world outside this container
EXPOSE 1337

# Run app.py when the container launches
CMD ["python", "app.py"]
