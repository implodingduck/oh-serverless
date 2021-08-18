import logging

import azure.functions as func
import os 
import json 

def main(req: func.HttpRequest, doc: func.DocumentList) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    for d in doc:
        logging.info(d)
    ratingId = req.route_params.get('ratingId')
    logging.info(ratingId)
    logging.info(f'{doc}')
    return func.HttpResponse(f"{doc}", status_code=200)
    
