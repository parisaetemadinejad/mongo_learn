# Aggregation in MongoDB is an operation used to process
# the data that returns the computed results.
import pymongo

my_connection = pymongo.MongoClient(host="localhost", port=27017)
my_db = my_connection["sample_database_4"]
my_col = my_db['blog']
list_data = [
    {
        "_id": 1,
        "firstName": "Jane",
        "lastName": "Doe",
        "phoneNumber": "555-555-1212",
        "city": "Beverly Hills",
        "state": "CA",
        "zip": 90210,
        "email": "Jane.Doe@compose.io"
    }

]
my_col.insert_many(list_data)
samples = my_col.find()
for _ in samples:
    print(_)
