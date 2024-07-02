# Use the latest TensorFlow GPU image as the base image
FROM tensorflow/tensorflow:latest-gpu

# Set the working directory
WORKDIR /app

# Copy requirements.txt to leverage Docker cache
COPY requirements.txt .

# Update and install required packages
RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-dev \
    build-essential \
    libpoppler-cpp-dev
    pkg-config \
    poppler-utils \
    tesseract-ocr \
    tesseract-ocr-eng \
    libtesseract-dev \
    git \
    ffmpeg \
    libsm6 \
    libxext6

# Upgrade pip
RUN pip3 install --upgrade pip

# Install Python packages from requirements.txt
RUN pip3 install -r requirements.txt

# Install detectron2 and other necessary packages
RUN pip3 install opencv-python-headless pyyaml==5.1
RUN pip3 install 'git+https://github.com/facebookresearch/fvcore'
RUN pip3 install 'git+https://github.com/facebookresearch/detectron2.git'
RUN pip3 install torchvision

# Add a new user "appuser" with the same user ID as the host user
ARG UID=1000
ARG GID=1000
RUN groupadd -g ${GID} appgroup && \
    useradd -m -u ${UID} -g appgroup -s /bin/bash appuser

# Switch to new user
USER appuser

# Copy the rest of the application code
COPY .. .

# Command to run your script
CMD ["python3", "extract_statistics.py"]
