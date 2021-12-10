from transformation import *
from ext_load import *
from db_connection import engine_connect_db
import logging

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

# Transformation of data
df_users = creating_user_df(jsonRespUser)
df_subscriptions = creating_subscriptions_df(jsonRespUser)
df_messages = creating_messages_df(jsonRespMessages)
logging.info(f"DataFrames created.")

# Load of the data into the dataBase
engine = engine_connect_db()
load_df(engine, df_users, 'users')
load_df(engine, df_subscriptions, 'subscriptions')
load_df(engine, df_messages, 'messages')
logging.info(f"Dataframes loaded into the Database.")

#alert of the end of the program
logging.info(f"Program Concluded.")
