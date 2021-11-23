#/bin/bash

docker build -t base-metadata-collector -f docker/Dockerfile-base .
docker build -t git-metadata-collector -f docker/Dockerfile .