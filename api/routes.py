from fastapi import APIRouter, Depends, HTTPException
from crawler.storage import books_collection, changes_collection
from .auth import get_api_key
from slowapi.util import get_remote_address
from slowapi import Limiter

limiter = Limiter(key_func=get_remote_address)
router = APIRouter(dependencies=[Depends(get_api_key)])

@router.get("/books")
@limiter.limit("20/minute")   # ✅ only 20 requests/minute per client
def list_books(category: str = None, min_price: float = 0, max_price: float = 9999,
               rating: int = None, sort_by: str = "price_incl_tax", page: int = 1, limit: int = 10):
    query = {"price_incl_tax": {"$gte": min_price, "$lte": max_price}}
    if category: query["category"] = category
    if rating: query["rating"] = rating

    cursor = books_collection.find(query).skip((page-1)*limit).limit(limit).sort(sort_by)
    return list(cursor)

@router.get("/books/{book_id}")
def get_book(book_id: str):
    book = books_collection.find_one({"_id": book_id})
    if not book:
        raise HTTPException(404, "Book not found")
    return book

@router.get("/changes")
def get_changes(limit: int = 50):
    return list(changes_collection.find().sort("at", -1).limit(limit))
