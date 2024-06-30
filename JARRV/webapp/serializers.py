from rest_framework import serializers
from .models import Item, Similar_Item, User, PurchaseHistory
from rest_framework_simplejwt.tokens import RefreshToken

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

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            'username', 
            'email', 
            'password', 
            'full_name', 
            'gender', 
            'total_water_saved', 
            'loyalty_points', 
            'total_amount_saved', 
            'user_id', 
            'account_creation'
        )
    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            full_name= validated_data['full_name'],
            gender=validated_data['gender'],
            # total_water_saved=0,
            # loyalty_points=0, 
            # total_amount_saved=0, 
        )
        return user
    

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

