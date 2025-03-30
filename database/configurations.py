from pymongo.mongo_client import MongoClient
# from pymongo.server_api import ServerApi

#* SERVER REMOTE : uri = "mongodb+srv://admin:admin@cluster0.fkefn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# client = MongoClient(uri, server_api=ServerApi('1'))

# Create a new client and connect to the server
# Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)

#* SERVER LOCAL :
client = MongoClient("localhost", 27017)

# 1. create db
db = client.algoretmia_db

# create collection
# todo = db.todo 
collection = db.algorithms

# FIXME
# TODO:  - Make a class to instanciate database local or remote
    # # insert a document

# from pymongo import MongoClient

# def database_connection():
#     root = "localhost"

#     client = MongoClient('localhost', 27017)

#     def __init__():
#         pass


#     def create_database():
#             # get the database
#         db = client.test # without schema or specific query we create the db

#         # create collection
#         todo = db.todo
