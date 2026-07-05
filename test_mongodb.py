from pymongo import MongoClient
uri = "mongodb+srv://praveen:<db_password>@auth.oytvu.mongodb.net/?appName=Auth"
client = MongoClient(uri)
try:
    client.admin.command("ping")
    print("Connected successfully")
    client.close()

except Exception as e:
    raise Exception(
        "The following error occurred: ", e)