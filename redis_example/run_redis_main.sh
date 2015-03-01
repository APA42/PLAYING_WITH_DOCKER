#!/bin/bash

#
#docker build -t python-redis-example-image .

# Create a container for redis
docker run --name redis-bote-container -d redis

# Create a container for python execution
# redis-bote-db => host bind at redis_main.py
docker run --name python-redis-example-container --link redis-bote-container:redis-bote-db   python-redis-example-image