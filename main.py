from etl import *

jsonRespUser = make_request('https://619ca0ea68ebaa001753c9b0.mockapi.io/evaluation/dataengineer/jr/v1/users')
jsonRespMessages = make_request('https://619ca0ea68ebaa001753c9b0.mockapi.io/evaluation/dataengineer/jr/v1/messages')


df_users = creating_user_df(jsonRespUser)
print(df_users)

df_subscriptions = creating_subscriptions_df(jsonRespUser)
print(df_subscriptions)

df_messages = creating_messages_df(jsonRespMessages)
print(df_messages)

engine = engine_connect_db()

load_user_df(engine, df_users)

load_subscriptions_df(engine, df_subscriptions)

load_messages_df(engine, df_messages)