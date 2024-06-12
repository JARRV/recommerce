from django.db import models


def get_upload_path(instance):
    return f'images/{instance.store}/'


class Item(models.Model):
    product_id = models.IntegerField(unique=True)
    store = models.CharField(max_length=200)
    item_name = models.CharField(max_length=200)
    picture = models.ImageField(upload_to=get_upload_path)
    brand = models.CharField(max_length=100)
    size = models.CharField(max_length=10)
    price = models.FloatField(max_length=3)
    sold = models.BooleanField(default=False)
    link = models.TextField()
    image_tags = models.TextField()

    def __str__(self):
        return self.item_name + " " + self.store + " " + self.price

    class Meta:
        ordering = ['store', 'item_name']
        verbose_name = 'Item'
        verbose_name_plural = 'Items'
        unique_together = ('product_id', 'store')
    
    

