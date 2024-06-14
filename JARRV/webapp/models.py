from django.db import models


def get_upload_path(instance):
    return f'images/{instance.store}/'


class Item(models.Model):
    store = models.CharField(max_length=200)
    item_name = models.CharField(max_length=200)
    item_type = models.CharField(max_length=200, default="Unknown")
    category = models.CharField(max_length=200, default="Unknown")
    picture_link = models.URLField(default="Unknown")
    brand = models.CharField(max_length=100)
    # size = models.CharField(max_length=10)
    price = models.FloatField(max_length=3)
    # sold = models.BooleanField(default=False)
    link = models.URLField(default="Unknown")
    # image_tags = models.TextField()

    def __str__(self):
        return f"{self.item_name}   {self.store}  {self.price}"

    class Meta:
        ordering = ['store', 'item_name']
        verbose_name = 'Item'
        verbose_name_plural = 'Items'
        # unique_together = ('product_id', 'store')
    
    

