# build the layer

#!/bin/bash -x

set -e
rm -rf layer
rm -rf *.zip

docker build -t cdu_query_lambda_layer .
CONTAINER=$(docker run -d cdu_query_lambda_layer false)
docker cp ${CONTAINER}:/layer.zip layer.zip