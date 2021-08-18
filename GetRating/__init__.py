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
    if len(doc) > 0:
        logging.info(f'{doc[0].to_json()}')
        retval = {
            'id': doc[0].get('id'),
            'userId': doc[0].get('userId'),
            'productId': doc[0].get('productId'),
            'timestamp': doc[0].get('timestamp'),
            'locationName': doc[0].get('locationName', ''),
            'rating': doc[0].get('rating'),
            'userNotes': doc[0].get('userNotes', ''),
        }
        return func.HttpResponse(f"{json.dumps(retval)}", status_code=200)
    else:
        return func.HttpResponse("{}", status_code=404)
    
