# Use the official Python image from the Docker Hub
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /service

# Copy the requirements file into the container
COPY requirements.txt requirements.txt

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the working directory contents into the container at /service
COPY . .

# Command to run the Gunicorn server
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "app:app"]