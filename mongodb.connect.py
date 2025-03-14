


import urllib.parse
from pymongo import MongoClient
from pymongo.server_api import ServerApi

# Encode credentials
username = urllib.parse.quote_plus("vijay")  # Make sure to use the correct user
password = urllib.parse.quote_plus("VIjaymuni55")  # Your real password here

# Correct cluster address (as you shared earlier)
cluster_address = "cluster0.aolvk.mongodb.net"

# Connection URI with /admin for authentication
uri = f"mongodb+srv://{username}:{password}@cluster0.aolvk.mongodb.net/admin?retryWrites=true&w=majority"
# uri = "mongodb+srv://<db_username>:<db_password>@cluster0.aolvk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"


# Connect MongoClient
client = MongoClient(uri, server_api=ServerApi("1"))

# Test connection
try:
    client.admin.command("ping")
    print("MongoDB connection successful!")
except Exception as e:
    print(f"MongoDB connection failed: {e}")
