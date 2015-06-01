#!/bin/bash
# Setup docker compose.

TDIR=`mktemp -d`
virtualenv $TDIR
. $TDIR/bin/activate
pip install docker-compose

export COMPOSE_PROJECT_NAME=payments_env_${JOB_NAME}_${BUILD_NUMBER}
export COMPOSE_FILE=../docker-compose-deploy.yml
docker-compose build;

# Delete virtualenv
rm -rf $TDIR
