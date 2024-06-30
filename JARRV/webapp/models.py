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
    size = models.CharField(max_length=30, choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'Extra Large'), ('XS', 'Extra Small'), ('XXL', 'Extra Extra Large')], blank=True, null=True, default="XS")

    def __str__(self):
        return f"{self.item_name} {self.store}"

    class Meta:
        ordering = ['store', 'item_name']
        # constraints = [
        #     models.UniqueConstraint(fields=['original_item_id', 'store', 'item_name'], name='unique_similar_item'),
        # ]

class User(models.Model):
    user_id = models.AutoField(primary_key=True) #how to populate
    username = models.CharField(max_length=200, unique=True)
    full_name = models.CharField(max_length=200)
    account_creation = models.DateField(auto_now_add=True) #how to populate
    password = models.CharField(max_length=200)
    gender = models.CharField(max_length=15, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], blank=True, null=True)
    email = models.EmailField(max_length=200, unique=True)
    total_water_saved = models.IntegerField(default=0)
    total_amount_saved = models.FloatField(max_length=3, default=0)
    loyalty_points = models.IntegerField(default=0)
    def __str__(self):
        return self.username
    
    @property
    def id(self):
        return self.user_id
    
    class Meta:
        ordering = ['username']
    

class PurchaseHistory(models.Model): #only when the purchase made is validated
    purchase_id = models.AutoField(primary_key=True)
    purchase_date = models.DateField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    item_id = models.ForeignKey(Similar_Item, on_delete=models.CASCADE)
    size = models.CharField(max_length=200)
    item_price = models.FloatField(max_length=3)
    amount_saved = models.FloatField(max_length=3)
    water_saved = models.IntegerField()
    loyalty = models.IntegerField()

    def __str__(self):
        return f"{self.purchase_id} {self.user_id}"
    
    class Meta:
        ordering = ['purchase_id']


