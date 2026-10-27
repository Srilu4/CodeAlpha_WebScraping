
import time

import pandas as pd
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"
SITE_ROOT = "https://books.toscrape.com/catalogue/"
RATING_MAP = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
HEADERS = {"User-Agent": "Mozilla/5.0 (CodeAlpha internship learning project)"}


def parse_page(html):
    """Extract all books from a single listing page."""
    soup = BeautifulSoup(html, "html.parser")
    books = []
    for item in soup.select("article.product_pod"):
        title = item.h3.a["title"]
        price = float(item.select_one("p.price_color").text.replace("£", "").replace("Â", ""))
        rating_word = item.select_one("p.star-rating")["class"][1]
        availability = item.select_one("p.instock.availability").text.strip()
        link = SITE_ROOT + item.h3.a["href"]
        books.append(
            {
                "title": title,
                "price_gbp": price,
                "rating": RATING_MAP.get(rating_word, None),
                "availability": availability,
                "url": link,
            }
        )
    return books


def scrape_all(max_pages=50):
    """Loop through every listing page and collect all books."""
    all_books = []
    for page in range(1, max_pages + 1):
        url = BASE_URL.format(page)
        response = requests.get(url, headers=HEADERS, timeout=15)
        if response.status_code != 200:
            print(f"Stopped at page {page} (status {response.status_code})")
            break
        books = parse_page(response.text)
        all_books.extend(books)
        print(f"Page {page}: {len(books)} books scraped (total {len(all_books)})")
        time.sleep(0.5)  # be polite to the server
    return all_books


def main():
    books = scrape_all()
    df = pd.DataFrame(books).drop_duplicates()
    df.to_csv("books.csv", index=False)
    print(f"\nSaved {len(df)} books to books.csv")
    print(df.head())
    print("\nAverage price:", round(df["price_gbp"].mean(), 2))
    print("Rating counts:\n", df["rating"].value_counts().sort_index())


if __name__ == "__main__":
    main()
