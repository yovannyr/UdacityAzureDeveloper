import azure.functions as func
import pymongo
import json
from bson.json_util import dumps
from bson.objectid import ObjectId
import logging

def main(req: func.HttpRequest) -> func.HttpResponse:

    # example call http://localhost:7071/api/getAdvertisement/?id=5eb6cb8884f10e06dc6a2084

    id = req.params.get('id')
    print("--------------->", id)
    
    if id:
        try:
            url = "mongodb://yrod-neighborlycosmosdbacount:YI40Y6gk9DUJX5P2HisXz5yh68dV4wz3uCu1CMtL0a8pwOiuK4D22FIi9q7Pc9Oqkt1INZeChWHD3FhwsAGuOQ==@yrod-neighborlycosmosdbacount.mongo.cosmos.azure.com:10255/?ssl=true&retrywrites=false&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@yrod-neighborlycosmosdbacount@"  
            client = pymongo.MongoClient(url)
            database = client['yrod-neighborlycosmosdb']
            collection = database['advertisements']
           
            query = {'_id': ObjectId(id)}
            result = collection.find_one(query)
            print("----------result--------")

            result = dumps(result)
            print(result)

            return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
        except:
            return func.HttpResponse("Database connection error.", status_code=500)

    else:
        return func.HttpResponse("Please pass an id parameter in the query string.", status_code=400)