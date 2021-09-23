import logging
import azure.functions as func
import pymongo
import json
import sys
from bson.json_util import dumps

 
def check_server_status(client):
   '''check the server status of the connected endpoint'''
   db = client.admin
   server_status = db.command('serverStatus')
   print('Database server status:')
   print(json.dumps(server_status, sort_keys=False, indent=2, separators=(',', ': ')))

def main(req: func.HttpRequest) -> func.HttpResponse:

    logging.info('Python getPosts trigger function processed a request.')

    try:
        url = "mongodb://yrod-neighborlycosmosdbacount:YI40Y6gk9DUJX5P2HisXz5yh68dV4wz3uCu1CMtL0a8pwOiuK4D22FIi9q7Pc9Oqkt1INZeChWHD3FhwsAGuOQ==@yrod-neighborlycosmosdbacount.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@yrod-neighborlycosmosdbacount@" 
        client = pymongo.MongoClient(url)
        check_server_status(client)
        database = client['yrod-neighborlycosmosdb']
        collection = database['posts']

        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8', status_code=200)
    except:
        return func.HttpResponse("Bad request.", status_code=400)