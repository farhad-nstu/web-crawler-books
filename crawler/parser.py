from bs4 import BeautifulSoup
from datetime import datetime
from hashlib import sha256
from .models import Book

async def parse_book_page(html, session):
    soup = BeautifulSoup(html, "lxml")
    books = []

    for book_div in soup.select(".product_pod"):
        title = book_div.h3.a["title"]
        link = book_div.h3.a["href"].replace("../../../", "")
        book_url = "https://books.toscrape.com/catalogue/" + link

        # Fetch detail page
        async with session.get(book_url) as resp:
            detail_html = await resp.text()

        detail_soup = BeautifulSoup(detail_html, "lxml")
        desc = detail_soup.select_one("#product_description ~ p")
        category = detail_soup.select("ul.breadcrumb li a")[-1].text
        price_incl = detail_soup.select_one(".price_color").text.strip("£")
        availability = detail_soup.select_one(".availability").text.strip()

        book = Book(
            name=title,
            description=desc.text if desc else None,
            category=category,
            price_incl_tax=float(price_incl),
            price_excl_tax=float(price_incl),  # adjust if needed
            availability=availability,
            num_reviews=0,
            image_url="https://books.toscrape.com/" + book_div.img["src"].replace("../", ""),
            rating=len(book_div.p["class"]) - 1 if book_div.p else 0,
            source_url=book_url,
            crawl_timestamp=datetime.utcnow(),
            raw_html=detail_html,
            fingerprint=sha256(detail_html.encode()).hexdigest()
        )
        books.append(book.dict())
    return books
