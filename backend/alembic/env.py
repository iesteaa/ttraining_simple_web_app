from logging.config import fileConfig

from alembic import context
from sqlalchemy import engine_from_config, pool

from app import models
from app.database import Base, database_url


config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

"""Alembic use table collection from DeclarativeBase"""
target_metadata = Base.metadata


def get_database_url() -> str:
    return database_url.render_as_string(hide_password=False)


def run_migrations_offline() -> None:
    """Generate migration SQL without opening a database connection."""

    context.configure(
        url=get_database_url(),
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        compare_type=True,
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations using a live database connection."""

    configuration = config.get_section(
        config.config_ini_section,
        {},
    )
    configuration["sqlalchemy.url"] = get_database_url()

    connectable = engine_from_config(
        configuration,
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
