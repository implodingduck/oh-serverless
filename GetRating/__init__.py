import logging

import azure.functions as func
from azure.cosmos import CosmosClient
import os 
import json 

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    ratingId = req.route_params.get('ratingId')
    connection_str = os.environ.get('AzureCosmosDBConnectionString')
    client = CosmosClient(connection_str)
    database_name = 'bfyocproductrating'
    database = client.get_database_client(database_name)
    container_name = 'ProductRating'
    container = database.get_container_client(container_name)
    query = 'SELECT * FROM ProductRating r WHERE r.id="{ratingId}"'
    retVal = {}
    for item in container.query_items(query=query, enable_cross_partition_query=True):
        print(f'{item}')
        retVal = item

    
    return func.HttpResponse(f"{json.dumps(retVal)}", status_code=200)
    
