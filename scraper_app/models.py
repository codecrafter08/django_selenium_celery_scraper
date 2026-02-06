from django.db import models

class Product(models.Model):
    site = models.CharField(max_length=50)
    title = models.TextField()
    price = models.CharField(max_length=50, null=True)
    url = models.URLField(unique=True)
    scraped_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
