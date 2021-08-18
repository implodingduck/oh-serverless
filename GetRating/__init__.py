import logging

import azure.functions as func
from azure.cosmos import CosmosClient
import os 
import json 

def main(req: func.HttpRequest, doc: func.DocumentList) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    ratingId = req.route_params.get('ratingId')
    print(ratingId)
    print(f'{doc}')
    return func.HttpResponse(f"{json.dumps(doc)}", status_code=200)
    
