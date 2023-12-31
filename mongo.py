from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()  # take environment variables from .env.

user = os.getenv('MONGO_USER')
password = os.getenv('MONGO_PASSWORD')

uri = f"mongodb+srv://{user}:{password}@cluster0.5tyuao5.mongodb.net/?retryWrites=true&w=majority"

#
# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

client.get_database('prueba').get_collection('Luis').insert_one(document={"marca": "opel", "modelo": "omega"})

"""
from pymongo.mongo_client import MongoClient
uri = "mongodb+srv://<username>:<password>@cluster0.5tyuao5.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri)
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
    
    """