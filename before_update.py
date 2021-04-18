# The PyMongo library allows interaction with the
# MongoDB database through Python; it is a native Python driver for MongoDB.
import pymongo

# create a DB
my_client = pymongo.MongoClient(host="localhost", port=27017)
# client = pymongo.MongoClient("mongodb://localhost:27017")
my_db = my_client["sample_database"]
# this code print list of DB
print(my_client.list_database_names())
# this code check if database exist in list of DB
db_list = my_client.list_database_names()
if "sample_database" in db_list:
    print("The database exists.")
else:
    print("no exist")
# create a collection
my_col = my_db["customers"]
# this code return list of collection such as table
print(my_db.list_collection_names())
# this code check list of collection
col_list = my_db.list_collection_names()
if "customers" in col_list:
    print("The collection exists.")
else:
    print("no exist")
# # we can insert some document to DB such as record
# my_dict_1 = {"name": "John", "address": "Highway 37"}
# my_dict_2 = {"name": "Peter", "address": "Lowstreet 27"}
# x_1 = my_col.insert_one(my_dict_1)
# x_2 = my_col.insert_one(my_dict_2)
# # this code print id of record
# print(x_1.inserted_id)
# print(x_2.inserted_id)
# ---------------------------------------------------------------------
# my note: In MongoDB, a collection is not created until it gets content!
# my note: In MongoDB, a document is not created until it gets content!
# ---------------------------------------------------------------------
# we can insert many document to collection
my_list = [
    {"_id": 1, "name": "John", "address": "Highway 37"},
    {"_id": 2, "name": "Peter", "address": "Lowstreet 27"},
    {"_id": 3, "name": "Amy", "address": "Apple st 652"},
    {"_id": 4, "name": "Hannah", "address": "Mountain 21"},
    {"_id": 5, "name": "Michael", "address": "Valley 345"},
    {"_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
    {"_id": 7, "name": "Betty", "address": "Green Grass 1"},
    {"_id": 8, "name": "Richard", "address": "Sky st 331"},
    {"_id": 9, "name": "Susan", "address": "One way 98"},
    {"_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
    {"_id": 11, "name": "Ben", "address": "Park Lane 38"},
    {"_id": 12, "name": "William", "address": "Central st 954"},
    {"_id": 13, "name": "Chuck", "address": "Main Road 989"},
    {"_id": 14, "name": "Viola", "address": "Sideway 1633"}
]
x = my_col.insert_many(my_list)

# print list of the _id values of the inserted documents:
# print(x.inserted_ids)
# find_one return first document of collection
# sample = my_col.find_one()
# print(sample)
# find return all document of collection
print('------------print a document of collection without filter-----------------------')
samples = my_col.find()
for _ in samples:
    print(_)
print('------------print a document of collection by filter-----------------------')
for x in my_col.find({"_id": 1, "name": 'John', "address": "Highway 37"}):
    print(x)
print('------------print a document of collection by filter just address so name is off------------')
for x in my_col.find({}, {"name": 0}):
    print(x)
# print('------------this code have error------------')why? i cant found
# for x in my_col.find({}, {"name": 1, "address": 0}):
#     print(x)
# When finding documents in a collection, you can filter the result by using a query object.

print('------------print a document of collection by filter address is "Park Lane 38"------------')
my_query = {"address": "Park Lane 38"}
my_doc = my_col.find(my_query)
for x in my_doc:
    print(x)
print('------------print a document of collection by filter start by letter S or letter higher ------------')
my_query = {"address": {"$gt": "S"}}

my_doc = my_col.find(my_query)

for x in my_doc:
    print(x)
print('------------print a document of collection by filter by regular Expressions ------------')
my_query = {"address": {"$regex": "^m"}}

my_doc = my_col.find(my_query)

for x in my_doc:
    print(x)
print('------------sort by name 1 refer asc and -1 refer desc------------')
my_doc = my_col.find().sort("name", -1)

for x in my_doc:
    print(x)
# The first parameter of the delete_one() method is a query object defining which document to delete.
# If the query finds more than one document, only the first occurrence is deleted.
# we write a query and delete base of query
my_col = my_db["customers"]
my_query = {"address": "Apple st 652"}
my_col.delete_one(my_query)
# we can delete many of row base of query
my_query = {"address": {"$regex": "^S"}}
x = my_col.delete_many(my_query)
print(x.deleted_count, " documents deleted.")
# delete all document in a collection
x = my_col.delete_many({})
print(x.deleted_count, " documents deleted.")
# we can use drop() method and drop a collection
my_col.drop()
