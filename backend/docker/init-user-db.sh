#!/bin/bash
set -e

# Modify pg_hba.conf to use trust authentication
echo "host all all all trust" >> /var/lib/postgresql/data/pg_hba.conf

# Restart PostgreSQL to apply changes
pg_ctl -D /var/lib/postgresql/data -l logfile restart

# Create the database
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "postgres" <<-EOSQL
    CREATE DATABASE stat_scribe;
EOSQL
