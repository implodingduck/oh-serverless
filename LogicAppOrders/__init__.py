import logging

import azure.functions as func
import requests
import json


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    post_data = {}
    try:
        req_body = req.get_json()
        for j in req_body:
            blob_url = j['content']['data']['blobUrl']
            if 'OrderHeaderDetails' in blob_url:
                post_data['orderHeaderDetailsCSVUrl'] = blob_url
            if 'OrderLineItems' in blob_url:
                post_data['orderLineItemsCSVUrl'] = blob_url
            if 'ProductInformation' in blob_url:
                post_data['productInformationCSVUrl'] = blob_url                                
        resp = requests.post('https://serverlessohmanagementapi.trafficmanager.net/api/order/combineOrderContent', data=json.dumps(post_data))
    except ValueError:
        pass


    return func.HttpResponse(
            f"{json.dumps(resp)}",
            status_code=200
    )
