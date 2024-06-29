from django.shortcuts import render
from rest_framework import generics

from .models import Item, Similar_Item, User, PurchaseHistory
from .serializers import ItemSerializer, SimilarItemSerializer, UserSerializer, PurchaseHistorySerializer

class ItemList(generics.ListCreateAPIView): #gets all the objects in the item database, needs some work in filtering here. 
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ItemDetail(generics.RetrieveUpdateDestroyAPIView): 
    queryset = Item.objects.all() 
    serializer_class = ItemSerializer
    lookup_field = 'item_id'

class SimilarItemDetails(generics.ListAPIView): #gets similar items with the inputted 
    serializer_class = SimilarItemSerializer
    lookup_field = 'original_item_id'
    def get_queryset(self):
        product_id = self.kwargs['original_item_id']  # Assuming 'author_id' is passed in URL
        queryset = Similar_Item.objects.filter(original_item_id_id=product_id)
        return queryset

class SimilarItemList(generics.ListCreateAPIView):
    queryset = Similar_Item.objects.all()
    serializer_class = SimilarItemSerializer

class SimilarItemInfo(generics.ListAPIView):
    # queryset = Similar_Item.objects.all()
    serializer_class = SimilarItemSerializer
    # lookup_field = 'item_id'
    def get_queryset(self):
        item_id = self.kwargs['item_id']
        queryset = Similar_Item.objects.filter(item_id=item_id)
        return queryset

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserInfo(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all() 
    serializer_class = UserSerializer
    lookup_field = 'user_id'

class AllPurchaseHistory(generics.ListAPIView):
    queryset = PurchaseHistory.objects.all()
    serializer_class = PurchaseHistorySerializer

class PurchaseHistoryDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseHistory.objects.all()
    serializer_class = PurchaseHistorySerializer
    lookup_field = 'purchase_id'

class UserPurchaseHistory(generics.ListAPIView):
    serializer_class = PurchaseHistory
    lookup_field = 'username'

    def get_queryset(self):
        username = self.kwargs('username')
        queryset = PurchaseHistory.objects.filter(username=username)
        return queryset

class ItemPurchaseHistory(generics.ListAPIView):
    serializer_class = PurchaseHistory
    lookup_field = 'item_id'

    def get_queryset(self):
        item_id = self.kwargs('item_id')
        queryset = PurchaseHistory.objects.filter(item_id_id=item_id)
