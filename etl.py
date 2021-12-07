import requests
import logging
from requests import HTTPError
import pandas as pd
from datetime import date, datetime
import sqlalchemy
from credentials import mysql_db_config
import sqlalchemy
from sqlalchemy import *

def make_request(url):
    try:
        responseUser = requests.get(url)
        responseUser = responseUser.json()
    except HTTPError as httpError:
        logging.warning(f'HTTP Error occored: {httpError}.')
        return 'Error'
    except Exception as err:
        logging.warning(f'Other error occored: {err}.')
        return 'Error'
    return responseUser



    

def creating_user_df(jsonRespUser):
    #flattening JSON and creating a df
    df_users = pd.json_normalize(jsonRespUser)

    # taking out personal information
    df_users['birthDate'] = pd.to_datetime(df_users['birthDate'])
    ## getting todays date
    today = date.today()
    today = pd.to_datetime('today')
    df_users['age'] =  (today.year - df_users['birthDate'].dt.year) - ((today.month - df_users['birthDate'].dt.month) < 0)
    ## extracting the domain
    df_users['domain'] = df_users['email'].str.split('@').str[1]
    ## dropping unwanted columns
    df_users = df_users.drop(columns=['firstName', 'lastName', 'address', 'zipCode', 'subscription', 'birthDate', 'email'])
    
    
    # making sure that the fields have the write ... int, datetime, bollean, string
    ## casting
    df_users['createdAt'] = pd.to_datetime(df_users['createdAt'])
    df_users['updatedAt'] = pd.to_datetime(df_users['updatedAt'])
    df_users['profile.isSmoking'] = df_users['profile.isSmoking'].astype('bool')
    df_users['profile.income'] = df_users['profile.income'].astype(float)
    df_users['id'] = df_users['id'].astype(int)
    df_users = df_users.rename(columns={'id': 'user_id'}, index={'ONE': 'Row_1'})
    df_users = df_users.rename(columns={'profile.income': 'profile_income'}, index={'ONE': 'Row_1'})
    df_users = df_users.rename(columns={'profile.isSmoking': 'profile_isSmoking'}, index={'ONE': 'Row_1'})
    df_users = df_users.rename(columns={'profile.gender': 'profile_gender'}, index={'ONE': 'Row_1'})
    df_users = df_users.rename(columns={'profile.profession': 'profile_profession'}, index={'ONE': 'Row_1'})
    ## reorganizign the fields
    df_users = df_users[['user_id','createdAt','updatedAt', 'city', 'country','domain','age','profile_gender','profile_isSmoking','profile_profession','profile_income']]
    return df_users




def creating_subscriptions_df(jsonRespUser):
    df_subscriptions = pd.json_normalize(jsonRespUser, meta=['id'], record_path=['subscription'])
    df_subscriptions['createdAt'] = pd.to_datetime(df_subscriptions['createdAt'])
    df_subscriptions['startDate'] = pd.to_datetime(df_subscriptions['startDate'])
    df_subscriptions['endDate'] = pd.to_datetime(df_subscriptions['endDate'])
    df_subscriptions['amount'] = df_subscriptions['amount'].astype(float)
    df_subscriptions = df_subscriptions.rename(columns={'status': 'status_subscription'}, index={'ONE': 'Row_1'})
    df_subscriptions['id'] = df_subscriptions['id'].astype(int)
    df_subscriptions = df_subscriptions.rename(columns={'id': 'user_id'}, index={'ONE': 'Row_1'})
    df_subscriptions["subscription_id"] = df_subscriptions.index + 1
    df_subscriptions = df_subscriptions[['subscription_id', 'createdAt', 'startDate', 'amount', 'status_subscription', 'user_id']]
    return df_subscriptions




def creating_messages_df(jsonRespMessages):
    df_messages = pd.json_normalize(jsonRespMessages)
    df_messages['createdAt'] = pd.to_datetime(df_messages['createdAt'])
    df_messages['id'] = df_messages['id'].astype(int)
    df_messages['receiverId'] = df_messages['receiverId'].astype(int)
    df_messages['senderId'] = df_messages['senderId'].astype(int)
    df_messages = df_messages.rename(columns={'id': 'message_id'}, index={'ONE': 'Row_1'})
    df_messages = df_messages.drop(columns=['message'])
    df_messages = df_messages[['message_id', 'createdAt', 'receiverId','senderId']]
    return df_messages



def engine_connect_db():
    engine = sqlalchemy.create_engine(f'mysql+pymysql://{mysql_db_config["user"]}:{mysql_db_config["password"]}@{mysql_db_config["host"]}') # connect to server

    #check if database exists if not add the database
    engine.execute(f"CREATE DATABASE IF NOT EXISTS {mysql_db_config['database']};") #create db

    #adding the database to the engine call
    engine = sqlalchemy.create_engine(f'mysql+pymysql://{mysql_db_config["user"]}:{mysql_db_config["password"]}@{mysql_db_config["host"]}/{mysql_db_config["database"]}')

    return engine




def load_user_df(engine, df_users):
    df_users.to_sql('users', engine, if_exists='replace', dtype={
    'user_id': Integer, 
    'createdAt': DateTime, 
    'updatedAt': DateTime, 
    'city': String(32),
    'country': String(32),
    'domain': String(32),
    'age': Integer,
    'profile_gender': String(32),
    'profile_isSmoking': Boolean,
    'profile_profession': String(100),
    'profile_income': Float},index=False)




def load_subscriptions_df(engine, df_subscriptions):
    df_subscriptions.to_sql('subscriptions', engine, if_exists='replace', dtype={ 
    'subscription_id': Integer, 
    'createdAt': DateTime, 
    'startDate': DateTime,
    'endDate': DateTime,
    'status_subscription': String(32),
    'amount': Float,
    'user_id': Integer},index=False)




def load_messages_df(engine, df_messages):
    df_messages.to_sql('messages', engine, if_exists='replace', dtype={
    'createdAt': DateTime, 
    'message_id': Integer, 
    'createdAt': DateTime, 
    'receiverId': String(32),
    'senderId': String(32)},index=False)