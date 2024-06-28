from django.contrib import admin
from .models import Item, Similar_Item, User, PurchaseHistory

# Register your models here.
admin.site.register(Item)
admin.site.register(Similar_Item)
admin.site.register(User)
admin.site.register(PurchaseHistory)