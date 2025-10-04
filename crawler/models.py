from pydantic import BaseModel, HttpUrl
from typing import Optional
from datetime import datetime

class Book(BaseModel):
    name: str
    description: Optional[str]
    category: str
    price_incl_tax: float
    price_excl_tax: float
    availability: str
    num_reviews: int
    image_url: HttpUrl
    rating: int
    source_url: HttpUrl
    crawl_timestamp: datetime
    raw_html: str
    fingerprint: str
