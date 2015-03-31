#!/bin/bash
set -e

NAME="docker_compose_example"
VERSION=`date +%Y%m%d%H%M%S`

docker build -t apa42/${NAME} .
docker tag -f apa42/${NAME} apa42/${NAME}:${VERSION}
