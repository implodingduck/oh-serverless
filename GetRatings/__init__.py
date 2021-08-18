import logging

import azure.functions as func
import os 
import json 

def main(req: func.HttpRequest, doc: func.DocumentList) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    
    logging.info(f'{doc}')
    retval = []
    for d in doc:
        logging.info(f'{d.to_json()}')
        retval.append({
            'id': d.get('id'),
            'userId': d.get('userId'),
            'productId': d.get('productId'),
            'timestamp': d.get('timestamp'),
            'locationName': d.get('locationName', ''),
            'rating': d.get('rating'),
            'userNotes': d.get('userNotes', ''),
        })
    return func.HttpResponse(f"{json.dumps(retval)}", status_code=200)
    
    
