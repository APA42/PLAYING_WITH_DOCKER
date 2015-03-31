#!/bin/bash
set -e

# access postgres database
export COMPONENT_DB_HOST_ADDR=$APA_BOTE_LINK_PORT_5432_TCP_ADDR
export COMPONENT_DB_TCP_PORT=$APA_BOTE_LINK_PORT_5432_TCP_PORT
export COMPONENT_DB_NAME=$APA_BOTE_LINK_ENV_POSTGRES_DB
export COMPONENT_DB_USER=$APA_BOTE_LINK_ENV_POSTGRES_USER
export COMPONENT_DB_PASSWORD=$APA_BOTE_LINK_ENV_POSTGRES_PASSWORD
# needed for migration
export MIGRATIONS_FOLDER=$PWD/postgres_access/migrations
# pythonpath
export PYTHONPATH=$PWD

case "$1" in
    "apa_run_main")
        shift
        OPTIONS="$@"
        # Wait to postgress startup
        sleep 7
        # Create database schema
        migrate
        # Run the app
        exec python apa_main.py
    ;;
esac
exec "$@"


