import azure.functions as func
import pymongo

def main(req: func.HttpRequest) -> func.HttpResponse:

    request = req.get_json()

    if request:
        try:
            url = "mongodb://yrod-neighborlycosmosdbacount:YI40Y6gk9DUJX5P2HisXz5yh68dV4wz3uCu1CMtL0a8pwOiuK4D22FIi9q7Pc9Oqkt1INZeChWHD3FhwsAGuOQ==@yrod-neighborlycosmosdbacount.mongo.cosmos.azure.com:10255/?ssl=true&retrywrites=false&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@yrod-neighborlycosmosdbacount@"  
            client = pymongo.MongoClient(url)
            database = client['yrod-neighborlycosmosdb']
            collection = database['advertisements']

            rec_id1 = collection.insert_one(eval(request))

            return func.HttpResponse(req.get_body())

        except ValueError:
            print("could not connect to mongodb")
            return func.HttpResponse('Could not connect to mongodb', status_code=500)

    else:
        return func.HttpResponse(
            "Please pass name in the body",
            status_code=400
        )