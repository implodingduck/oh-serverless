import logging

import azure.functions as func
import requests


# {
#   "userId": "cc20a6fb-a91f-4192-874d-132493685376",
#   "productId": "4c25613a-a3c2-4ef3-8e02-9c335eb23204",
#   "locationName": "Sample ice cream shop",
#   "rating": 5,
#   "userNotes": "I love the subtle notes of orange in this ice cream!"
# }


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')


    try:
        req_body = req.get_json()
        if 'userId' not in req_body:
            return func.HttpResponse("userId is required", status_code=400)
    except ValueError:
        return func.HttpResponse("something went wrong", status_code=500)
    

    return func.HttpResponse(
            "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
            status_code=200
    )
