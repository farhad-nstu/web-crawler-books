import aiohttp
import asyncio
from .parser import parse_book_page

BASE_URL = "https://books.toscrape.com"

async def fetch(session, url):
    async with session.get(url) as response:
        if response.status == 200:
            return await response.text()
        return None

async def crawl_books(pages=2):
    books = []
    async with aiohttp.ClientSession() as session:
        for page in range(1, pages + 1):
            url = f"{BASE_URL}/catalogue/page-{page}.html"
            html = await fetch(session, url)
            if not html:
                continue
            page_books = await parse_book_page(html, session)
            books.extend(page_books)
    return books

if __name__ == "__main__":
    all_books = asyncio.run(crawl_books(pages=1))
    print(f"Crawled {len(all_books)} books")
    for book in all_books[:2]:
        print(book["name"], book["price_incl_tax"])