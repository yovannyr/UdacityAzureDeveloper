import azure.functions as func
import pymongo
import json
from bson.json_util import dumps

def main(req: func.HttpRequest) -> func.HttpResponse:

    try:
        url = "mongodb://yrod-neighborlycosmosdbacount:YI40Y6gk9DUJX5P2HisXz5yh68dV4wz3uCu1CMtL0a8pwOiuK4D22FIi9q7Pc9Oqkt1INZeChWHD3FhwsAGuOQ==@yrod-neighborlycosmosdbacount.mongo.cosmos.azure.com:10255/?ssl=true&retrywrites=false&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@yrod-neighborlycosmosdbacount@"  
        client = pymongo.MongoClient(url)
        database = client['yrod-neighborlycosmosdb']
        collection = database['advertisements']


        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
    except:
        print("could not connect to mongodb")
        return func.HttpResponse("could not connect to mongodb",
                                 status_code=400)

