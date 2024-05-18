const { MongoClient } = require("mongodb");

// Replace the uri string with your MongoDB deployment's connection string.

const uri = "mongodb+srv://yeon_lee:1234@cluster0.6j64or2.mongodb.net/"

const client = new MongoClient(uri);

async function run() {

  try {

    await client.connect();

    db = client.sample
    coll = db.people
    
    const cursor = coll.find();

    // iterate code goes here

    await cursor.forEach(console.log);

  } finally {

    // Ensures that the client will close when you finish/error

    await client.close();

  }

}

run().catch(console.dir);