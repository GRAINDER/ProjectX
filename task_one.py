from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.cursor import Cursor
from typing import Dict, Any

def filter_documents(collection: Collection, filter_criteria: Dict[str, Any]) -> Cursor:
    pipeline = [
        {
            '$match': filter_criteria
        }
    ]
    return collection.aggregate(pipeline)

# Establish a connection to the MongoDB server
client = MongoClient('mongodb://localhost:27017')
db = client['STOCK']
collection = db['Supplier']

# Define the filter criteria
criteria = {'status': 'inactive'}

# Call the filter_documents function
result = filter_documents(collection, criteria)

# Iterate over the cursor and print the filtered documents
for doc in result:
    print(doc)