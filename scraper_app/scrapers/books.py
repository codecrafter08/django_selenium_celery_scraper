from selenium.webdriver.common.by import By
from .base import BaseScraper

class BooksScraper(BaseScraper):
    def parse(self):
        cfg = self.config["listing"]
        
        # Capture H1 as requested
        h1_text = self.get_h1()
        print(f"Page H1: {h1_text}")
        
        cards = self.driver.find_elements(By.CSS_SELECTOR, cfg["product_card"])
        products = []

        for card in cards:
            title = self.get_attr(card, cfg["title"], "title") # Title is in the title attribute of the 'a' tag
            if not title:
                title = self.get_text(card, cfg["title"])
            
            price = self.get_text(card, cfg["price"])
            link = self.get_attr(card, cfg["link"], "href")

            if title and link:
                # Append H1 to title to show we captured it, if user wants it
                full_title = f"[{h1_text}] {title}" if h1_text else title
                
                products.append({
                    "site": "books",
                    "title": full_title,
                    "price": price,
                    "url": link
                })
        
        return products

    def run(self):
        self.fetch(self.config["url"])
        data = self.parse()
        self.close()
        return data
