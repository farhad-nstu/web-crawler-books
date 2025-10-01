from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(os.getenv("MONGO_URI", "mongodb://localhost:27017"))
db = client[os.getenv("MONGO_DB", "books_db")]
books_collection = db["books"]
changes_collection = db["changes"]

def save_book(book):
    existing = books_collection.find_one({"source_url": book["source_url"]})
    if existing:
        if existing["fingerprint"] != book["fingerprint"]:
            books_collection.update_one(
                {"_id": existing["_id"]},
                {"$set": book}
            )
            changes_collection.insert_one({
                "book_id": existing["_id"],
                "change": "updated",
                "field": "content",
                "at": book["crawl_timestamp"]
            })
    else:
        result = books_collection.insert_one(book)
        changes_collection.insert_one({
            "book_id": result.inserted_id,
            "change": "new",
            "at": book["crawl_timestamp"]
        })
