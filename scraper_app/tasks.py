import os
from celery import shared_task
from django.conf import settings

from scraper_app.scrapers.registry import SCRAPER_REGISTRY
from scraper_app.services import save_products

@shared_task(bind=True, autoretry_for=(Exception,), retry_backoff=10)
def run_scraper_task(self, site):
    if site not in SCRAPER_REGISTRY:
        raise ValueError("Unknown site")

    config_path = os.path.join(
        settings.BASE_DIR,
        "scraper_app/configs",
        f"{site}.yaml",
    )

    scraper_class = SCRAPER_REGISTRY[site]
    scraper = scraper_class(config_path)

    data = scraper.run()
    save_products(data)

    return f"{site} completed with {len(data)} items"
