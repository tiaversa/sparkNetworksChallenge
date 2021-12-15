import pandas as pd
from datetime import date

def creating_user_df(jsonRespUser):
    # flattening JSON and creating a df
    df_users = pd.json_normalize(jsonRespUser, sep='_')
    # taking out personal information
    df_users["birthDate"] = pd.to_datetime(df_users["birthDate"])
    df_users["birth_year"] = ( df_users["birthDate"].dt.year)
    df_users["domain"] = df_users["email"].str.split("@").str[1]
    df_users = df_users.drop(
        columns=["firstName","lastName","address","zipCode","subscription", "birthDate","email"]
    )
    ## casting
    df_users["createdAt"] = pd.to_datetime(df_users["createdAt"])
    df_users["updatedAt"] = pd.to_datetime(df_users["updatedAt"])
    df_users = df_users.rename(columns={"id": "user_id"}, index={"ONE": "Row_1"})
    return df_users


def creating_subscriptions_df(jsonRespUser):
    df_subscriptions = pd.json_normalize(
        jsonRespUser, meta=["id"], record_path=["subscription"], sep='_'
    )
    df_subscriptions["createdAt"] = pd.to_datetime(df_subscriptions["createdAt"])
    df_subscriptions["startDate"] = pd.to_datetime(df_subscriptions["startDate"])
    df_subscriptions["endDate"] = pd.to_datetime(df_subscriptions["endDate"])
    df_subscriptions = df_subscriptions.rename(
        columns={"status": "status_subscription"}, index={"ONE": "Row_1"}
    )
    df_subscriptions = df_subscriptions.rename(
        columns={"id": "user_id"}, index={"ONE": "Row_1"}
    )
    df_subscriptions["subscription_id"] = df_subscriptions.index + 1
    return df_subscriptions


def creating_messages_df(jsonRespMessages):
    df_messages = pd.json_normalize(jsonRespMessages)
    df_messages["createdAt"] = pd.to_datetime(df_messages["createdAt"])
    df_messages = df_messages.rename(
        columns={"id": "message_id"}, index={"ONE": "Row_1"}
    )
    df_messages = df_messages.drop(columns=["message"])
    return df_messages