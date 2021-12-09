import requests
import logging
from requests import HTTPError
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
        logging.warning(f"HTTP Error occored: {httpError}.")
        return "Error"
    except Exception as err:
        logging.warning(f"Other error occored: {err}.")
        return "Error"
    return responseUser


def load_df(engine, df, name):
    try:
        df.to_sql(
            name,
            engine,
            if_exists="replace",
            index=False,
        )
    except Exception as err:
        logging.warning(f"Other error occored: {err}.")




# An HTTP POST for output
def post_data(df):
    dataset = df.to_json()
    post_data = {'dataset ID': "makis", 'date start': "1", 'date end': "2", 'payload': dataset}
    url = "http://localhost:8081/upload_dataset"
    #r = requests.post(url, json=post_data)
    print(dataset)

