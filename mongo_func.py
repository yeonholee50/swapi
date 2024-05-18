import random_people_swap
from pymongo import MongoClient


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
    print(result.inserted_ids)
    client.close()

def find():
    client = get_database()
    db = client.sample
    coll = db.people
    coll.drop()
    cursor = coll.find()
    for doc in cursor:
        print(doc)
    client.close() 

def main():
    populate()
    find()
    

if __name__ == "__main__":
    main()
