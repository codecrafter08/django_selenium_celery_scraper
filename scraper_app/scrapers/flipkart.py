from selenium.webdriver.common.by import By
from .base import BaseScraper

class FlipkartScraper(BaseScraper):
    def parse(self):
        cfg = self.config["listing"]
        cards = self.driver.find_elements(By.CSS_SELECTOR, cfg["link"])

        products = []

        for card in cards:
            title = self.get_text(card, cfg["title"])
            price = self.get_text(card, cfg["price"])
            link = card.get_attribute("href")

            if title and link:
                products.append({
                    "site": "flipkart",
                    "title": title,
                    "price": price,
                    "url": link,
                })

        return products

    def run(self):
        self.fetch(self.config["url"])
        data = self.parse()
        self.close()
        return data
