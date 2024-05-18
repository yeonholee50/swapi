import random_people_swap
from pymongo import MongoClient

"""
api calls especially to rapid have ahrad limit so why not store these odds into a common database instead of doing multiple api calls 
for ones that have a hard limit.
"""
def get_database():
    connection_string = "mongodb+srv://yeon_lee:1234@cluster0.6j64or2.mongodb.net/"
    client = MongoClient(connection_string)
    return client
def populate():
    response = random_people_swap.main()
    client = get_database()
    db = client.sample
    coll = db.people
    coll.drop()
    result = coll.insert_many([response])
    client.close()
    return result.inserted_ids

def find():
    client = get_database()
    db = client.sample
    coll = db.people
    cursor = coll.find()
    """
    for doc in cursor:
        print(doc)
    """
    client.close() 
    return cursor

def main():
    populate()
    find()
    

if __name__ == "__main__":
    main()
