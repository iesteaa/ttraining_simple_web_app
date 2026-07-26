#SQLALCHEMY ENGINE
# involved : Current used DB, driver, address of DB, get connection, connection pool. 


from sqlalchemy import URL, create_engine
from app.config import settings

database_url = URL.create(
    drivername="postgresql+psycopg", #dialect,driver
    username=settings.postgres_user,
    password=settings.postgres_password,
    host=settings.postgres_host,
    port=settings.postgres_port,
    database=settings.postgres_db,
)

#core connection backend x DB
engine= create_engine(database_url) #connection pool 
