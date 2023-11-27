

# How to Run Server for Client


## Setup configuration

The docker-compose file has several variables that need to be set, in the docker-compose.yaml file.
You may have already been given this file seperately, if so, please use it as it's ready for you.

- DB_ENGINE=django.db.backends.mysql
- DB_HOST=**URL of the MySQL Server**
- DB_PORT=**Port of the MySQL server**
- DB_DATABASE=legosumo_db
- DB_USER=**MySQL User**
- DB_PASSWORD=**MySQL User Password**
- PRODUCTION=**True** or **False** to run without Django Debugging interface

## Running Server on Windows

1. Install Docker Desktop
2. Start windows Terminal App
3. Run `docker-compose up --build`

## Running Server on Linux

1. Install Docker `apt-get update && apt-get install docker docker-compose`
2. Run `docker-compose up --build`
