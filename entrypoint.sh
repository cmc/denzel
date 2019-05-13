#!/bin/sh
# Generic Docker-Compose wait for PG entrypoint

waitforpg () {
        POSTGRES_PASSWORD=$(cat config/config.json | python -c 'import sys, json; print(json.load(sys.stdin)["POSTGRES_PASSWORD"])')
        until PGPASSWORD=$POSTGRES_PASSWORD psql -h "$POSTGRES_HOST" -d "$POSTGRES_DB" -U "$POSTGRES_USER" -c '\q'; do
          >&2 echo "Postgres is unavailable - sleeping..."
          sleep 3
        done
        >&2 echo "Postgres is up - Starting."
        sleep 3
}


if [ -n "$ENTRYPOINT_CMD" ]; then

        if [ -n "$DEBUG" ]; then
          loglevel=debug
  else
          loglevel=info 
  fi
  case $ENTRYPOINT_CMD in
    denzel )
        python run.py ;;
    worker )
       PWD=/src/ celery worker -A workers.comparator --loglevel=debug ;;    
    * )
            echo "ERROR: Invalid Entrypoint $ENTRYPOINT_CMD."
        exit 1 ;;
  esac  
else
  echo "ERROR: No entrypoint provided."
  exit 1
fi
