#!/bin/bash
#
# Runs unit_tests
#

# Create a temporary virtualenv to install docker-compose
TDIR=`mktemp -d`
virtualenv $TDIR
. $TDIR/bin/activate
pip install docker-compose

export COMPOSE_PROJECT_NAME=pay
COMPOSE_CMD="docker-compose jenkins${JOB_NAME}${BUILD_NUMBER} -f ../docker-compose-deploy.yml"
$COMPOSE_CMD build;

# Delete virtualenv
rm -rf $TDIR
