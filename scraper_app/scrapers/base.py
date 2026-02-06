import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class BaseScraper:
    def __init__(self, config_path):
        with open(config_path) as f:
            self.config = yaml.safe_load(f)

        import os
        from pathlib import Path
        
        if os.name == 'posix':
            cache_dir = Path("/tmp/.wdm")
        else:
            cache_dir = Path(__file__).resolve().parent.parent.parent / ".wdm"
            
        cache_dir.mkdir(parents=True, exist_ok=True)
        os.environ["WDM_LOCAL"] = "1"
        os.environ["WDM_CACHE"] = str(cache_dir)
        os.environ["WDM_CACHE_PATH"] = str(cache_dir)

        options = Options()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36")

        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options,
        )

    def fetch(self, url):
        self.driver.get(url)
        import time
        try:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(3)
            self.driver.execute_script("window.scrollTo(0, 0)")
            time.sleep(2)
        except Exception:
            pass

        wait_selector = self.config.get("wait_for")
        if wait_selector:
            try:
                WebDriverWait(self.driver, 30).until(
                    EC.presence_of_element_located(
                        (By.CSS_SELECTOR, wait_selector)
                    )
                )
            except Exception:
                pass

    def get_h1(self):
        try:
            return self.driver.find_element(By.TAG_NAME, "h1").text
        except:
            return None

    def get_text(self, parent, selector):
        try:
            return parent.find_element(By.CSS_SELECTOR, selector).text
        except:
            return None

    def get_attr(self, parent, selector, attr):
        try:
            return parent.find_element(
                By.CSS_SELECTOR, selector
            ).get_attribute(attr)
        except:
            return None

    def close(self):
        self.driver.quit()
