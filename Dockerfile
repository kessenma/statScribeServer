# Use the latest TensorFlow GPU image as the base image
FROM tensorflow/tensorflow:latest-gpu

# Update and install required packages
RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-dev \
    build-essential \
    libpoppler-cpp-dev \
    pkg-config \
    poppler-utils

# Upgrade pip
RUN pip3 install --upgrade pip

# Install Python packages
RUN pip3 install torch transformers pymupdf pandas pdfminer.six

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Command to run your script
CMD ["python3", "extract_statistics.py"]
