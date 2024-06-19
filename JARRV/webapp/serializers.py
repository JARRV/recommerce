from rest_framework import serializers
from .models import Item, Similar_Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class SimilarItemSerializer(serializers.ModelSerializer):
    original_item_id = serializers.CharField(source='original_item_id.item_id', read_only=True)
    class Meta:
        model = Similar_Item
        fields = '__all__'