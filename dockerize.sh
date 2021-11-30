#/bin/bash

docker build -t base-metadata-collector -f docker/Dockerfile-base .
docker build -t git-metadata-collector -f docker/Dockerfile-metadata .
docker build -t git-code-complexity -f docker/Dockerfile-code-complexity .


docker run \
  -v /home/tng/Documents/facebook/grimoirlab/git-metadata-collector/out:/results \
  -v /home/tng/Documents:/scan_folder \
  git-metadata-collector \
  --scan-path /scan_folder --out-folder /results