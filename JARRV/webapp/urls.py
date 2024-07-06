from django.urls import path
from .views import ItemList, ItemDetail, SimilarItemList, SimilarItemDetails, index

urlpatterns = [
    path("", index, name='index'),
    path("items/", ItemList.as_view(), name='item_list'),
    path("items/<str:item_id>/", ItemDetail.as_view(), name='item_detail'), 
    path("similar_items/", SimilarItemList.as_view(), name='similar_item_list'),
    path("similar_items/<str:original_item_id>/", SimilarItemDetails.as_view(), name='similar_item_detail'),

]