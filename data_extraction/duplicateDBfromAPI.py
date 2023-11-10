# Pip Library
import pymongo
import logging
# User Library
import api

# Setting up logging
logging.basicConfig(filename="api.log", filemode="w", level=20)

# Connecting to Database
mclient = pymongo.MongoClient("mongodb://localhost:27017")

# Drop Database if already existing
if "MET" in mclient.list_database_names():
    mclient.drop_database("MET")

db = mclient["MET"]

deps = api.getDepartments()

for department in deps['departments']:

    name = department['displayName']
    dep_id = department['departmentId']

    # Set MongoDB Collection to Department id
    db_col = db[str(dep_id)]

    ids = api.getObjectsfromDepartment(dep_id)
    total = ids['total']

    for i, id in enumerate(ids['objectIDs']):
        try:
            data = api.getObjectJSON(id)
            
            # Replace ID for MongoDB
            data["_id"] = data.pop("objectID")
            
            # Add to Current collection
            db_col.insert_one(data)
            
            if(i % 100 == 0):
                text = f"{dep_id}/{len(deps['departments'])}      {i}/{total}     Done"
                print(text)

        except Exception as e:
            logging.error(f"{dep_id}, {name}, {id}:     {e}")





