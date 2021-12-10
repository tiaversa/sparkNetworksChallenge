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
        response_req = requests.get(url).json()
        #response_req = response_req.json()
    except HTTPError as httpError:
        logging.warning(f"HTTP Error occored: {httpError}.")
        return "Error"
    except Exception as err:
        logging.warning(f"Other error occored: {err}.")
        return "Error"
    return response_req


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