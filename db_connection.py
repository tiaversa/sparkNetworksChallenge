import sqlalchemy
from credentials import mysql_db_config

def engine_connect_db():
    engine = sqlalchemy.create_engine(
        f'mysql+pymysql://{mysql_db_config["user"]}:{mysql_db_config["password"]}@{mysql_db_config["host"]}'
    )  # connect to server

    # check if database exists if not add the database
    engine.execute(
        f"CREATE DATABASE IF NOT EXISTS {mysql_db_config['database']};"
    )  # create db

    # adding the database to the engine call
    engine = sqlalchemy.create_engine(
        f'mysql+pymysql://{mysql_db_config["user"]}:{mysql_db_config["password"]}@{mysql_db_config["host"]}/{mysql_db_config["database"]}'
    )

    return engine