from django.db import models

def get_upload_path(instance):
    return f'images/{instance.store}/'

def get_default_item_id():
    return "default_item_id"

def get_default_item():
    default_item, created = Item.objects.get_or_create(
        item_id="default_item_id",  # This should be a valid unique ID
        defaults={
            'store': 'default_store',
            'item_name': 'Default Item',
            'item_type': 'Default Type',
            'category': 'Default Category',
            'picture_link': 'http://example.com/default.jpg',
            'brand': 'Default Brand',
            'price': 0.0,
            'link': 'http://example.com/default',
        }
    )
    return default_item.item_id  # Ensure this returns the primary key

class Item(models.Model):
    item_id = models.CharField(max_length=200, primary_key=True, default=get_default_item_id)
    store = models.CharField(max_length=200)
    item_name = models.CharField(max_length=200)
    item_type = models.CharField(max_length=200, default="Unknown")
    category = models.CharField(max_length=200, default="Unknown")
    picture_link = models.URLField(default="http://example.com/default.jpg")
    brand = models.CharField(max_length=100)
    price = models.FloatField(max_length=3)
    link = models.URLField(default="http://example.com/default")
    # water_consumption = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.item_name} {self.store}"

    class Meta:
        ordering = ['store', 'item_name']
        verbose_name = 'Item'
        verbose_name_plural = 'Items'
        constraints = [
            models.UniqueConstraint(fields=['item_id'], name='unique_item_id')
        ]

class Similar_Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    original_item_id = models.ForeignKey(Item, on_delete=models.CASCADE, default=get_default_item)  # This should be a callable returning a valid primary key
    store = models.CharField(max_length=400)
    item_name = models.CharField(max_length=400)
    picture_link = models.URLField(default="http://example.com/default.jpg")
    price = models.CharField(max_length=200)
    link = models.URLField(default="http://example.com/default")
    size = models.CharField(max_length=400, default="XS")

    def __str__(self):
        return f"{self.item_name} {self.store}"

    class Meta:
        ordering = ['store', 'item_name']
        # constraints = [
        #     models.UniqueConstraint(fields=['original_item_id', 'store', 'item_name'], name='unique_similar_item'),
        # ]
