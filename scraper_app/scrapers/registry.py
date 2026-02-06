from .flipkart import FlipkartScraper
from .books import BooksScraper

SCRAPER_REGISTRY = {
    "flipkart": FlipkartScraper,
    "books": BooksScraper,
}
