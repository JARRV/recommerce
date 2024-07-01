from django.urls import path
from .views import ItemList, ItemDetail, SimilarItemList, SimilarItemDetails, SimilarItemInfo, UserList, UserInfo, AllPurchaseHistory, PurchaseHistoryDetails, UserPurchaseHistory, ItemPurchaseHistory,LoginView, RegisterView

urlpatterns = [
    path("items/", ItemList.as_view(), name='item_list'), #all original items
    path("items/<str:item_id>/", ItemDetail.as_view(), name='item_detail'),  #info about specific item
    path("similar_items/", SimilarItemList.as_view(), name='similar_item_list'), # all similar items
    path("similar_items/<str:original_item_id>/", SimilarItemDetails.as_view(), name='similar_item_detail'), #all similar items for specific original item
    path("similar_items/info/<int:item_id>", SimilarItemInfo.as_view(), name='similar_item_info'), # info about a specific similar item
    path("users/", UserList.as_view(), name='user_list'), #all users 
    path("users/<int:user_id>",UserInfo.as_view(), name="user_info"),  #information about a specific user
    path("purchase_history/", AllPurchaseHistory.as_view(), name="all_purchase_history"), #all purchases 
    path("purchase_history/<int:purchase_id>", PurchaseHistoryDetails.as_view(), name="purchase_history_details"), #details about a specific purchase
    path ("purchase_history/user/<int:user_id>", UserPurchaseHistory.as_view(), name="user_purchase_history"), #purchases of a specific user
    path("purchase_history/item/<int:item_id>", ItemPurchaseHistory.as_view(), name="item_purchase_history"),#specific item purchase
    path('signup/', RegisterView.as_view(), name='user_register'), 
    path('signin/', LoginView.as_view(), name='user_login'),

]