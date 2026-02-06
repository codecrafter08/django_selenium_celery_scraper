from .models import Product

def save_products(products):
    for p in products:
        Product.objects.update_or_create(
            url=p["url"],
            defaults={
                "site": p["site"],
                "title": p["title"],
                "price": p["price"],
            },
        )
