#!/bin/bash

# Navigate to the directory containing your Dockerfile and Python script
cd /home/gpt15/Desktop/statScribeServer/backend/ExtractionAlgorithms/

# Build the Docker image if necessary
docker build --build-arg UID=$(id -u) --build-arg GID=$(id -g) -t scibert-extractor .

# Run the Docker container with the mounted volumes and user settings
docker run --gpus all \
    -v /home/gpt15/Desktop/statScribeServer/backend/test2.pdf:/app/test2.pdf \
    -v /home/gpt15/Desktop/statScribeServer/backend/outputs:/app/outputs \
    --user $(id -u):$(id -g) \
    scibert-extractor
