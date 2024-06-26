#!/bin/bash

# Navigate to the directory containing your Dockerfile and Python script
cd /home/gpt15/Desktop/statScribeServer

# Build the Docker image if necessary
docker build -t scibert-extractor .

# Run the Docker container with the mounted volumes
docker run --gpus all -v /home/gpt15/Desktop/statScribeServer/test2.pdf:/app/test2.pdf -v /home/gpt15/Desktop/statScribeServer/outputs:/app/outputs scibert-extractor
