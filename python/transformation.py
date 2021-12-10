import pandas as pd
from datetime import date
from expode_log import add_log

def creating_user_df(jsonRespUser):
    # flattening JSON and creating a df
    df_users = pd.json_normalize(jsonRespUser, sep='_')
    # taking out personal information
    df_users["birthDate"] = pd.to_datetime(df_users["birthDate"])
    ## getting todays date
    today = date.today()
    today = pd.to_datetime("today")
    df_users["age"] = (today.year - df_users["birthDate"].dt.year) - (
        (today.month - df_users["birthDate"].dt.month) < 0
    )
    ## extracting the domain
    df_users["domain"] = df_users["email"].str.split("@").str[1]
    ## dropping columns for PII compliance and unwanted ones too
    df_users = df_users.drop(
        columns=[
            "firstName",
            "lastName",
            "address",
            "zipCode",
            "subscription",
            "birthDate",
            "email",
        ]
    )
    # making sure that the fields have the right ... int, datetime, bollean, string
    ## casting
    df_users["createdAt"] = pd.to_datetime(df_users["createdAt"])
    df_users["updatedAt"] = pd.to_datetime(df_users["updatedAt"])
    df_users["profile_isSmoking"] = df_users["profile_isSmoking"].astype("bool")
    df_users["profile_income"] = df_users["profile_income"].astype(float)
    df_users["age"] = df_users["age"].astype(int)
    df_users["id"] = df_users["id"].astype(int)
    df_users = df_users.rename(columns={"id": "user_id"}, index={"ONE": "Row_1"})
    ## reorganizign the fields
    df_users = df_users[
        [
            "user_id",
            "createdAt",
            "updatedAt",
            "city",
            "country",
            "domain",
            "age",
            "profile_gender",
            "profile_isSmoking",
            "profile_profession",
            "profile_income",
        ]
    ]
    return df_users


def creating_subscriptions_df(jsonRespUser):
    jsonRespUser = add_log(jsonRespUser)
    df_subscriptions = pd.json_normalize(
        jsonRespUser, meta=["id"], record_path=["subscription"], sep='_'
    )
    df_subscriptions["createdAt"] = pd.to_datetime(df_subscriptions["createdAt"])
    df_subscriptions["startDate"] = pd.to_datetime(df_subscriptions["startDate"])
    df_subscriptions["endDate"] = pd.to_datetime(df_subscriptions["endDate"])
    df_subscriptions["amount"] = df_subscriptions["amount"].astype(float)
    df_subscriptions = df_subscriptions.rename(
        columns={"status": "status_subscription"}, index={"ONE": "Row_1"}
    )
    df_subscriptions["id"] = df_subscriptions["id"].astype(int)
    df_subscriptions = df_subscriptions.rename(
        columns={"id": "user_id"}, index={"ONE": "Row_1"}
    )
    df_subscriptions["subscription_id"] = df_subscriptions.index + 1
    df_subscriptions["subscription_id"] = df_subscriptions["subscription_id"].astype(int)
    # shift column 'Name' to first position
    first_column = df_subscriptions.pop("subscription_id")
    # insert column using insert(position,column_name,first_column) function
    df_subscriptions.insert(0, "subscription_id", first_column)
    second_column = df_subscriptions.pop("user_id")
    df_subscriptions.insert(1, "user_id", second_column)
    return df_subscriptions


def creating_messages_df(jsonRespMessages):
    df_messages = pd.json_normalize(jsonRespMessages)
    
    df_messages["createdAt"] = pd.to_datetime(df_messages["createdAt"])
    df_messages["id"] = df_messages["id"].astype(int)
    df_messages["receiverId"] = df_messages["receiverId"].astype(int)
    df_messages["senderId"] = df_messages["senderId"].astype(int)
    df_messages = df_messages.rename(
        columns={"id": "message_id"}, index={"ONE": "Row_1"}
    )
    df_messages = df_messages.drop(columns=["message"])
    df_messages = df_messages[["message_id", "createdAt", "receiverId", "senderId"]]
    return df_messages