#!/bin/bash

if [ ! -f .env ]; then
    echo "ERROR: missing '.env' file."
    echo "SOLUTION: run \`cp env.template .env\` and complete '.env' \
    (use POSTGRES_HOST=localhost)."
    exit 1
fi

source .env
DOCKER_NAME="myFastAPI-DB"

docker stop $(docker ps -aqf "name=${DOCKER_NAME}")
docker rm $(docker ps -aqf "name=${DOCKER_NAME}")

# Create and start the PostgreSQL container
docker run \
    --name ${DOCKER_NAME} \
    -e POSTGRES_HOST_AUTH_METHOD=trust \
    -p ${POSTGRES_PORT}:5432 \
    -d postgres

# Wait a few seconds for the container to start
sleep 3

# Create custom user and database in the PostgreSQL container
docker exec -it ${DOCKER_NAME} psql \
    -U postgres \
    -c "CREATE USER \"$POSTGRES_USER\" WITH PASSWORD '$POSTGRES_PASSWORD';"
docker exec -it ${DOCKER_NAME} psql \
    -U postgres \
    -c "CREATE DATABASE \"$POSTGRES_DB\" OWNER '$POSTGRES_USER';"
