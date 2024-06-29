from rest_framework import serializers
from .models import Item, Similar_Item, User, PurchaseHistory


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class SimilarItemSerializer(serializers.ModelSerializer):
    original_item_id = serializers.CharField(source='original_item_id.item_id', read_only=True)
    class Meta:
        model = Similar_Item
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class PurchaseHistorySerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(source='user_id.user_id', read_only=True)
    item_id = serializers.IntegerField(source='item_id.item_id', read_only=True)

    class Meta:
        model= PurchaseHistory
        fields = '__all__'