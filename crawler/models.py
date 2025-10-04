from pydantic import BaseModel, Field, HttpUrl
from typing import Optional
from datetime import datetime

class Book(BaseModel):
    name: str = Field(..., example="The Great Gatsby")
    description: Optional[str] = Field(None, example="A classic novel set in the 1920s.")
    category: str = Field(..., example="Fiction")
    price_incl_tax: float = Field(..., example=15.99)
    price_excl_tax: float = Field(..., example=13.50)
    availability: str = Field(..., example="In stock")
    num_reviews: int = Field(..., example=256)
    image_url: HttpUrl = Field(..., example="https://example.com/images/book.jpg")
    rating: int = Field(..., example=5)
    source_url: HttpUrl = Field(..., example="https://example.com/book-page")
    crawl_timestamp: datetime = Field(..., example="2025-10-04T12:30:00Z")
    raw_html: str = Field(..., example="<html>...</html>")
    fingerprint: str = Field(..., example="abc123def456")

