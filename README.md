# CodeAlpha_WebScraping

**CodeAlpha Data Analytics Internship - Task 1: Web Scraping**

## Objective
Collect a custom dataset from a public website using Python, so it can be used later for analysis and visualization.

## Website
[books.toscrape.com](https://books.toscrape.com), a sandbox site made for scraping practice (1000 books across 50 pages).

## Data collected
| Column | Description |
|---|---|
| title | Book title |
| price_gbp | Price in British pounds |
| rating | Star rating (1 to 5) |
| availability | Stock status |
| url | Link to the book page |

## Tools
- Python 3
- `requests` to download pages
- `BeautifulSoup` to parse the HTML
- `pandas` to build and save the dataset

## How it works
1. Loop through listing pages 1 to 50.
2. For each page, download the HTML with `requests`.
3. Use CSS selectors in `BeautifulSoup` to pull out title, price, rating, availability and link.
4. Convert the star-rating word (One, Two, ...) into a number.
5. Wait 0.5 seconds between requests to be polite to the server.
6. Combine everything into a pandas DataFrame, remove duplicates and save to `books.csv`.

## How to run
```bash
pip install -r requirements.txt
python scraper.py
```

## Output
`books.csv` with about 1000 rows.

## Key learnings
- Reading HTML structure with browser Inspect tool
- Handling pagination
- Cleaning scraped values (currency symbols, rating words)
- Scraping responsibly with delays and a User-Agent header

## Next steps
This dataset can be reused for Exploratory Data Analysis (price vs rating) and Data Visualization tasks.
