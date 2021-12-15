from transformation import *
from ext_load import *
from db_connection import engine_connect_db
import logging

def extract_center():
# Getting Logging to print on console
    logging.basicConfig(level = logging.INFO)
    # Extraction by requests
    jsonRespUser = make_request(
        "https://619ca0ea68ebaa001753c9b0.mockapi.io/evaluation/dataengineer/jr/v1/users"
    )
    jsonRespMessages = make_request(
        "https://619ca0ea68ebaa001753c9b0.mockapi.io/evaluation/dataengineer/jr/v1/messages"
    )
    if ((jsonRespUser == 'Not found')or(jsonRespMessages == 'Not found')):
        logging.warning(f"Request unsucessuful. Endpoint not found.")
    else:
        logging.info(f"JSON Loaded.")
    return [jsonRespUser, jsonRespMessages]

def transform_center(jsonResp):
    # Transformation of data
    df_users = creating_user_df(jsonResp[0])
    df_subscriptions = creating_subscriptions_df(jsonResp[0])
    df_messages = creating_messages_df(jsonResp[1])
    logging.info(f"DataFrames created.")
    return [df_users, df_subscriptions, df_messages]

def load_center(engine, df_list):
# Load of the data into the dataBase
    load_df(engine, df_list[0], 'users')
    load_df(engine, df_list[1], 'subscriptions')
    load_df(engine, df_list[2], 'messages')
    logging.info(f"Dataframes loaded into the Database.")



# main app
my_engine = engine_connect_db()
jsonResp = extract_center()
df_list = transform_center(jsonResp)
load_center(my_engine, df_list)
#alert of the end of the program
logging.info(f"Program Concluded.")
