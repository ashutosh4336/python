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

# Get the total No number of Documens as per parsed filetr
count = collection.count_documents({})
# document = []
# document.append({
#     'name': 'Sonam Chaubey',
#     'age': 24,
#     'city': 'Jabalpur',
#     'occuption': 'Intern',
#     'technology': 'Javascript'
# })
#
# document.append({
#     'name': 'Ashutosh Panda',
#     'age': 21,
#     'city': 'Bhubaneswar',
#     'occuption': 'Intern',
#     'technology': 'MEAN Stack'
# })

# response = collection.insert_many(document)

# filter = {
#     'technology': 'MEAN Stack'
# }
filter = {
    'name': 'Ashutosh Panda'
}

response = collection.find(filter)
# lastinserted_ids = response.inserted_ids
print(count)
for el in response:
    print(f'Data : {el}')
