# docker build -t canyoufindme .
# docker run -d -p 7000:7000 "IMAGEID"

# Use a Python base image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the Python script into the container
COPY app.py /app/app.py
COPY flag.txt /app/flag.txt

EXPOSE 7000

# Install dependencies, if any
# Example: RUN pip install <dependency_name>

# Start the Python script
CMD ["python", "app.py"]
