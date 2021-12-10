from ext_load import *
#Unit testing

#testing the try/exception for requests
jsonRespUser = make_request(
    "19ca0ea68ebaa001753c9b0.mockapi.io/evaluation/dataengineer/jr"
)
jsonRespMessages = make_request(
    "https://619ca0ea68ebaa001753c9b0.mockapi.io/evaluation/dataengineer/jr/v1/messages"
)
if ((jsonRespUser == 'Not found')or(jsonRespMessages == 'Not found')):
    logging.warning(f"Request unsucessuful. Endpoint not found.")
else:
    logging.info(f"JSON Loaded.")