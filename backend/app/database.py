# SQLALCHEMY ENGINE
# involved : Current used DB, driver, address of DB, get connection, connection pool.
from collections.abc import Generator

from sqlalchemy import URL, create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

from app.config import settings


class Base(DeclarativeBase):
    pass


database_url = URL.create(
    drivername="postgresql+psycopg",  # dialect,driver
    username=settings.postgres_user,
    password=settings.postgres_password,
    host=settings.postgres_host,
    port=settings.postgres_port,
    database=settings.postgres_db,
)

# core connection backend x DB
engine = create_engine(database_url)  # connection pool

SessionLocal = sessionmaker(bind=engine)


def get_db() -> Generator[Session]:
    db = SessionLocal()

    try:
        yield db  # open session, and connection still on after the endpoint
        # so the procces remain, and could be continue

    finally:  # close sesion
        db.close()
