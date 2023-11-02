#!/bin/bash

if [ ! -f .env ]; then
    echo "ERROR: missing '.env' file."
    echo "SOLUTION: run \`cp env.template .env\` and complete '.env'"
    exit 1
fi

source .env

if [ "$POSTGRES_HOST" != "localhost" ]; then
    echo "ERROR: POSTGRES_HOST is '$POSTGRES_HOST' and not 'localhost'"
    exit 1
fi

pgVars="POSTGRES_PORT POSTGRES_USER POSTGRES_PASSWORD POSTGRESS_DB"
for var in $pgVars; do
    if [ -z "${!var}" ]; then
        echo "ERROR: missing $var in '.env' file."
        exit 1
    fi
done

DOCKER_NAME="myFastAPI-DB"

docker stop $(docker ps -aqf "name=${DOCKER_NAME}")
docker rm $(docker ps -aqf "name=${DOCKER_NAME}")

docker run \
    --name ${DOCKER_NAME} \
    --env POSTGRES_HOST_AUTH_METHOD=trust \
    --publish ${POSTGRES_PORT}:5432 \
    --detach postgres

sleep 3

docker exec --interactive --tty ${DOCKER_NAME} psql \
    --username postgres \
    --command "CREATE USER \"$POSTGRES_USER\" WITH PASSWORD '$POSTGRES_PASSWORD';"

docker exec --interactive --tty ${DOCKER_NAME} psql \
    --username postgres \
    --command "CREATE DATABASE \"$POSTGRES_DB\" OWNER '$POSTGRES_USER';"
