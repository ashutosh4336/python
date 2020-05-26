from pymongo import MongoClient
# import pymongo

connstring = "mongodb+srv://ashutosh123:ashutosh123@ashutosh4336-tybmp.mongodb.net/pyapp?retryWrites=true&w=majority"
# connstring = 'mongodb://127.0.0.1:27017/pyapp'
# client = pymongo.MongoClient(connstring)

client = MongoClient(connstring)
# db = client.test

# Get all the Database in the ATLAS instance
# print(client.list_database_names())

# Select a Database Name
dbinstance = client.get_database('pyapp')

# Retrive all the collection in the DB
# print(dbinstance.list_collection_names())


collection = dbinstance.get_collection('users')


# document = []
# document.append({
#     'name': 'Divya Tyagi',
#     'age': 24,
#     'city': 'Jammu Kashmir',
#     'occuption': 'Software Developer',
#     'technology': 'MERN Stack'
# })
#
# document.append({
#     'name': 'Amit Khanduri',
#     'age': 89,
#     'city': 'Africa',
#     'occuption': 'Peon',
#     'technology': 'Admin'
# })


# Filter
# filter = {
#     'technology': 'MEAN Stack'
# }

# filter = {
#     'name': 'Ashutosh Panda'
# }

# response = collection.insert_many(document)
# response = collection.find()
# response = collection.find().sort('age', 1)
# response = collection.delete_one({"name": "Shruti Gupta"})

# lastinserted_ids = response.inserted_ids


# Get the total No number of Documens as per parsed filetr
count = collection.count_documents({})
print(count)


# print(response)

for el in response:
    print(f'Data : {el}')
