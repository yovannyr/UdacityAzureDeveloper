import azure.functions as func
import pymongo
from bson.objectid import ObjectId


def main(req: func.HttpRequest) -> func.HttpResponse:

    id = req.params.get('id')

    if id:
        try:
            url = "mongodb://yrod-neighborlycosmosdbacount:YI40Y6gk9DUJX5P2HisXz5yh68dV4wz3uCu1CMtL0a8pwOiuK4D22FIi9q7Pc9Oqkt1INZeChWHD3FhwsAGuOQ==@yrod-neighborlycosmosdbacount.mongo.cosmos.azure.com:10255/?ssl=true&retrywrites=false&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@yrod-neighborlycosmosdbacount@"  
            client = pymongo.MongoClient(url)
            database = client['yrod-neighborlycosmosdb']
            collection = database['advertisements']
            
            query = {'_id': ObjectId(id)}
            result = collection.delete_one(query)
            return func.HttpResponse("")

        except:
            print("could not connect to mongodb")
            return func.HttpResponse("could not connect to mongodb", status_code=500)

    else:
        return func.HttpResponse("Please pass an id in the query string",
                                 status_code=400)
