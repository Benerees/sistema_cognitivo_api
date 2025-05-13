#!/bin/bash

# Aguarda o MongoDB iniciar completamente
sleep 5

# Faz a importação do arquivo JSON
mongoimport \
  --username "$MONGO_INITDB_ROOT_USERNAME" \
  --password "$MONGO_INITDB_ROOT_PASSWORD" \
  --authenticationDatabase admin \
  --db "$MONGO_INITDB_DATABASE" \
  --collection event_logs \
  --jsonArray \
  --file /docker-entrypoint-initdb.d/dump_event_logs.json
