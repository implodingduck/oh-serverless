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
        retval = {
            'id': doc[0]['id'],
            'userId': doc[0]['userId'],
            'productId': doc[0]['productId'],
            'rating': doc[0]['rating'],
            'userNotes': doc[0]['userNotes'],
            'locationName': doc[0]['locationName'],
            'timestamp': doc[0]['timestamp']
        }
        return func.HttpResponse(f"{retval}", status_code=200)
    else:
        return func.HttpResponse("{}", status_code=404)
    
