import pymongo

my_client = pymongo.MongoClient("mongodb://localhost:27017/")
my_db = my_client["my_database_2"]
my_col = my_db["customers"]
# my_list = [
#     {"_id": 1, "name": "John", "address": "Highway 37"},
#     {"_id": 2, "name": "Peter", "address": "Lowstreet 27"},
#     {"_id": 3, "name": "Amy", "address": "Apple st 652"},
#     {"_id": 4, "name": "Hannah", "address": "Mountain 21"},
#     {"_id": 5, "name": "Michael", "address": "Valley 345"},
#     {"_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
#     {"_id": 7, "name": "Betty", "address": "Green Grass 1"},
#     {"_id": 8, "name": "Richard", "address": "Sky st 331"},
#     {"_id": 9, "name": "Susan", "address": "One way 98"},
#     {"_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
#     {"_id": 11, "name": "Ben", "address": "Park Lane 38"},
#     {"_id": 12, "name": "William", "address": "Central st 954"},
#     {"_id": 13, "name": "Chuck", "address": "Main Road 989"},
#     {"_id": 14, "name": "Viola", "address": "Sideway 1633"}
# ]
# x = my_col.insert_many(my_list)
my_query = {"address": "Valley 345"}
new_values = {"$set": {"address": "Canyon 123"}}

my_col.update_one(my_query, new_values)

# print "customers" after the update:
for x in my_col.find():
    print(x)
print('--------update many items----------------')
my_query = {"address": {"$regex": "^S"}}
new_values = {"$set": {"name": "Minnie"}}

x = my_col.update_many(my_query, new_values)

print(x.modified_count, "documents updated.")
print('--------use limit in mongo----------------')
my_result = my_col.find().limit(3)

# print the result:
for x in my_result:
    print(x)
