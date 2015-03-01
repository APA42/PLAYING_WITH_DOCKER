# Examples of programs written in python and executed with docker

## Versions used
###Docker version
Client version: 1.5.0

Client API version: 1.17

###Boot2docker version:
Boot2Docker-cli version: v1.5.0

Git commit: ccd9032

## Redis example
An example using redis for data persistence
 
### 1 - Create docker image of your python program
```
docker build -t python-redis-example-image .
``

### 2 - Execution with Docker
#### We need a container for redis
```
docker run --name redis-bote-container -d redis
```

#### Now we need to execute our program in a container based in our image and linked to redis-container
```
docker run --name python-redis-example-container --link redis-bote-container:redis-bote-db redis-python-image
```

Notice that we need to update REDIS_SERVER_URI at redis_main.py in order to use <i>redis-bote-db</i>