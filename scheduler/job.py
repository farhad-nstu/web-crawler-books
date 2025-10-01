from apscheduler.schedulers.blocking import BlockingScheduler
import asyncio
from crawler.scraper import crawl_books
from crawler.storage import save_book

def run_crawler():
    async def main():
        books = await crawl_books(pages=2)
        for book in books:
            save_book(book)
        print(f"Crawled and saved {len(books)} books")
    asyncio.run(main())

def start_scheduler():
    scheduler = BlockingScheduler()
    scheduler.add_job(run_crawler, "interval", hours=24)
    print("Scheduler started (every 24h)")
    scheduler.start()

if __name__ == "__main__":
    run_crawler()   # run once
    # start_scheduler()   # use this for continuous schedule
