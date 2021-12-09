from transformation import *
from ext_load import *
from db_connection import engine_connect_db
import logging
import luigi

# Extraction by requests
jsonRespUser = make_request(
    "https://619ca0ea68ebaa001753c9b0.mockapi.io/evaluation/dataengineer/jr/v1/users"
)
jsonRespMessages = make_request(
    "https://619ca0ea68ebaa001753c9b0.mockapi.io/evaluation/dataengineer/jr/v1/messages"
)
logging.warning(f"JSON Loaded.")

# Transformation of data
df_users = creating_user_df(jsonRespUser)
df_subscriptions = creating_subscriptions_df(jsonRespUser)
df_messages = creating_messages_df(jsonRespMessages)
logging.warning(f"DataFrames created.")


# Load of the data into the dataBase
engine = engine_connect_db()
load_df(engine, df_users, 'users')
load_df(engine, df_subscriptions, 'subscriptions')
load_df(engine, df_messages, 'messages')
logging.warning(f"Dataframes loaded into the Database.")

#Post as output
post_data(df_users)

#alert of the end of the program
logging.warning(f"Program Concluded.")
