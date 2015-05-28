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
```

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

## Docker Compose example
An example using docker-compose, python and postgres

Its use two container. One for postgres database and the other for python application.
Creation of database schema is done using simpledatamigrate 

https://github.com/aleasoluciones/simpledatamigrate

The application insert five elements to the database (alias bote) and query for all elements

### Build and tag the image
```
./build_image_and_tag.sh
```

### Run
```
docker-compose up -d
```

See the logs

```
docker-compose logs
```

### Optional. Connect directly to postgres
Uncomment ports in docker-compose.yml file

```
psql --host=POSTGRES_CONTAINER_IP --port 5432 --username=postgres --password --dbname=inventory
```

POSTGRES_CONTAINER_IP == ip of the container or ip of boot2docker for mac

## Share host local time with containers (MacOsx)

### Situation
If you try to share localtime you'll probably receive an error

```
$>docker run --rm -v /etc/localtime:/etc/localtime:ro debian date
```

```
FATA[0000] Error response from daemon: Cannot start container 20538e53a0d9d: [8] System error: not a directory
```

### What I do
Your home directory is shared to Boot2Docker (Virtual Machine) at /Users/MyUser. The idea is to share the localtime file


#### Does not work :-( 
At your home directory create a link /etc/localtime of to your real machine

```
/Users/MyUser>ln -s /etc/localtime localtime
```

#### This works
Copy your /etc/localtime file to your home directory

```
/Users/MyUser>cp /etc/localtime localtime
```

#### Continue
Enter into boot2docker virtual machine

```
$>boot2docker ssh
```

If /etc/localtime exists as directory, move it

```
docker@boot2docker: sudo mv  /etc/localtime/ /etc/localtime.ORG/
```

Copy localtime file

```
docker@boot2docker: sudo cp  /Users/MyUser/localtime /etc/localtime
```

### Test it
Run a container and check the date. Have to be the same as your computer

```
$>docker run --rm -v /etc/localtime:/etc/localtime:ro debian date
```

