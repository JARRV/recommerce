from django.shortcuts import render
from rest_framework import generics

from .models import Item, Similar_Item
from .serializers import ItemSerializer, SimilarItemSerializer

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

