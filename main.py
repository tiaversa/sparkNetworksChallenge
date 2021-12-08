from etl import *
from db_connection import engine_connect_db

# Extraction by requests
jsonRespUser = make_request(
    "https://619ca0ea68ebaa001753c9b0.mockapi.io/evaluation/dataengineer/jr/v1/users"
)
jsonRespMessages = make_request(
    "https://619ca0ea68ebaa001753c9b0.mockapi.io/evaluation/dataengineer/jr/v1/messages"
)

# Transformation of data
df_users = creating_user_df(jsonRespUser)
df_subscriptions = creating_subscriptions_df(jsonRespUser)
df_messages = creating_messages_df(jsonRespMessages)


# Load of the data into the dataBase
engine = engine_connect_db()
load_user_df(engine, df_users)
load_subscriptions_df(engine, df_subscriptions)
load_messages_df(engine, df_messages)
