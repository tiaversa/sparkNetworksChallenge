from sqlalchemy import *
from credentials import mysql_db_config

def creting_tables_messages(engine):
    meta = MetaData()

    messages = Table(
    'messages', meta, 
    Column('message_id', Integer), 
    Column('createdAt', DateTime),
    Column('receiverId', Integer), 
    Column('senderId', Integer)
    )
    meta.create_all(bind=engine, tables=[messages],checkfirst=True)


def creting_tables_subscriptions(engine):
    meta = MetaData()

    subscriptions = Table(
    'subscriptions', meta, 
    Column('subscription_id', Integer), 
    Column('user_id', Integer),   
    Column('createdAt', DateTime), 
    Column('startDate', DateTime),
    Column('endDate', DateTime), 
    Column('status_subscription', String(15)), 
    Column('amount', Float)
    )
    meta.create_all(bind=engine, tables=[subscriptions],checkfirst=True)


def creting_tables_users(engine):
    meta = MetaData()

    users = Table(
    'users', meta, 
    Column('user_id', Integer), 
    Column('createdAt', DateTime), 
    Column('updatedAt', DateTime),
    Column('city', String(32)),
    Column('country', String(32)), 
    Column('domain', String(20)), 
    Column('birth_year', Integer),   
    Column('profile_gender', String(8)), 
    Column('profile_isSmoking', Boolean),
    Column('profile_profession', String(32)),
    Column('profile_income', Float)   
    )
    meta.create_all(bind=engine, tables=[users],checkfirst=True)

def create_tables(engine):
    creting_tables_users(engine)
    creting_tables_subscriptions(engine)
    creting_tables_messages(engine)



def engine_connect_db():
    engine = create_engine(
        f'mysql+pymysql://{mysql_db_config["user"]}:{mysql_db_config["password"]}@{mysql_db_config["host"]}'
    )  # connect to server

    # check if database exists if not add the database
    engine.execute(
        f"CREATE DATABASE IF NOT EXISTS {mysql_db_config['database']};"
    )  # create db

    # adding the database to the engine call
    engine = create_engine(
        f'mysql+pymysql://{mysql_db_config["user"]}:{mysql_db_config["password"]}@{mysql_db_config["host"]}/{mysql_db_config["database"]}'
    )
    create_tables(engine)

    return engine