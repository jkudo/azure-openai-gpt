# Use an official Python runtime as a parent image
FROM python:3.11-slim-bullseye

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install build tools and any needed packages specified in requirements.txt
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc && \
    pip install --no-cache-dir -r requirements.txt && \
    apt-get purge -y --auto-remove gcc && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Make port 80 available to the world outside this container
# EXPOSE 80

# Define environment variable
ENV OPENAI_API_BASE=<your_openai_api_base>
ENV OPENAI_API_KEY=<your_openai_api_key>

# Run app.py when the container launches
CMD ["python", "app.py"]
