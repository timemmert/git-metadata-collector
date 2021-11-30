#/bin/bash

docker build -t base-metadata-collector -f docker/Dockerfile-base .
docker build -t git-metadata-collector -f docker/Dockerfile .

docker run \
  -v /home/tng/Documents/facebook/grimoirlab/git-metadata-collector/out:/analysis \
  -v /home/tng/Documents/facebook/grimoirlab/git-metadata-collector/demo:/scan_folder \
  git-metadata-collector \
  --scan-path /scan_folder --out-folder /analysis