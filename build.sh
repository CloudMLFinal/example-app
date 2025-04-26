#!/bin/bash
docker build -t example-app -f DockerFile .
if [ $? -eq 0 ]; then
    echo "Docker image built successfully!"
else
    echo "Docker build failed!"
    exit 1
fi 