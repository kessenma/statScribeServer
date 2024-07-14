# backend/db/alembic/env.py
from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool, create_engine, text

from alembic import context

from backend.db.models.models import Base


target_metadata = Base.metadata

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support

from backend.db.models.user_accounts import User
from backend.db.models.extracted_stats import Statistics

# Set target_metadata to the metadata of your models
target_metadata = Base.metadata  # Assuming all models use the same Base

def create_database():
    """Create the database if it doesn't exist."""
    # Connect to the default 'postgres' database to create 'statscribe'
    engine = create_engine("postgresql://statscribe:ss123@localhost:5434/postgres")
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1 FROM pg_database WHERE datname = 'statscribe'"))
        exists = result.scalar() is not None

        if not exists:
            conn.execute(text("COMMIT"))
            conn.execute(text("CREATE DATABASE statscribe"))

def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.
    """
    # Ensure the database exists
    create_database()

    # Connect to the 'statscribe' database
    engine = create_engine("postgresql://statscribe:ss123@localhost:5434/statscribe")
    connectable = engine

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
