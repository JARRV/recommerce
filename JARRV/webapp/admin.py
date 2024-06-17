from django.contrib import admin
from .models import Item, Similar_Item

# Register your models here.
admin.site.register(Item)
admin.site.register(Similar_Item)