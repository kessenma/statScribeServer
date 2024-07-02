#!/bin/bash

# Configuration variables
DB_NAME="research_app"
DB_USER="statscribe"
DB_PASS="ss123"

# Function to create the database and user
function create_database() {
    sudo -u postgres psql -c "CREATE DATABASE $DB_NAME;"
    sudo -u postgres psql -c "CREATE USER $DB_USER WITH ENCRYPTED PASSWORD '$DB_PASS';"
    sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE $DB_NAME TO $DB_USER;"
    echo "Database $DB_NAME and user $DB_USER have been created."
}

# Function to drop the database
function drop_database() {
    sudo -u postgres psql -c "DROP DATABASE IF EXISTS $DB_NAME;"
    sudo -u postgres psql -c "DROP USER IF EXISTS $DB_USER;"
    echo "Database $DB_NAME and user $DB_USER have been dropped."
}

# Main program logic
if [ "$1" == "create" ]; then
    create_database
elif [ "$1" == "drop" ]; then
    drop_database
else
    echo "Usage: $0 {create|drop}"
fi
