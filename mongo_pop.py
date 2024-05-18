import random_people_swap
from pymongo import MongoClient


def get_database():
    connection_string = "mongodb+srv://yeon_lee:1234@cluster0.6j64or2.mongodb.net/"
    client = MongoClient(connection_string)
    return client
def main():
    response = random_people_swap.main()
    client = get_database()
    db = client.sample
    coll = db.people
    coll.drop()
    result = coll.insert_many([response])
    print(result.inserted_ids)
    client.close()
    

if __name__ == "__main__":
    main()
