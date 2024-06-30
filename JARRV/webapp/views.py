from django.shortcuts import render
from rest_framework import generics, status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
import bcrypt

from .models import Item, Similar_Item, User, PurchaseHistory
from .serializers import ItemSerializer, SimilarItemSerializer, UserSerializer, PurchaseHistorySerializer, RegisterSerializer, LoginSerializer

class ItemList(generics.ListCreateAPIView): #gets all the objects in the item database, needs some work in filtering here. 
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [AllowAny]
    authentication_classes = []

class ItemDetail(generics.RetrieveUpdateDestroyAPIView): 
    queryset = Item.objects.all() 
    serializer_class = ItemSerializer
    lookup_field = 'item_id'
    permission_classes =[AllowAny]
    authentication_classes = []

class SimilarItemDetails(generics.ListAPIView): #gets similar items with the inputted 
    serializer_class = SimilarItemSerializer
    lookup_field = 'original_item_id'
    permission_classes =[AllowAny]
    authentication_classes = []
    def get_queryset(self):
        product_id = self.kwargs['original_item_id']  # Assuming 'author_id' is passed in URL
        queryset = Similar_Item.objects.filter(original_item_id_id=product_id)
        return queryset

class SimilarItemList(generics.ListCreateAPIView):
    queryset = Similar_Item.objects.all()
    serializer_class = SimilarItemSerializer
    permission_classes =[AllowAny]
    authentication_classes = []
    


class SimilarItemInfo(generics.ListAPIView):
    # queryset = Similar_Item.objects.all()
    serializer_class = SimilarItemSerializer
    authentication_classes = []
    permission_classes =[AllowAny]
    # lookup_field = 'item_id'
    def get_queryset(self):
        item_id = self.kwargs['item_id']
        queryset = Similar_Item.objects.filter(item_id=item_id)
        return queryset

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [IsAdminUser]
    # authentication_classes = [IsAdminUser]

class UserInfo(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all() 
    serializer_class = UserSerializer
    lookup_field = 'user_id'
    authentication_classes = [IsAuthenticated, IsAdminUser]
    permission_classes = [IsAdminUser]

class AllPurchaseHistory(generics.ListAPIView):
    queryset = PurchaseHistory.objects.all()
    serializer_class = PurchaseHistorySerializer
    # authentication_classes=[IsAdminUser]
    # permission_classes = [IsAdminUser]

class PurchaseHistoryDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseHistory.objects.all()
    serializer_class = PurchaseHistorySerializer
    lookup_field = 'purchase_id'
    # permission_classes = [IsAdminUser]

class UserPurchaseHistory(generics.ListAPIView):
    serializer_class = PurchaseHistory
    lookup_field = 'username'
    # authentication_classes = [IsAuthenticated, IsAdminUser]
    # permission_classes = [IsAdminUser, IsAuthenticated]

    def get_queryset(self):
        username = self.kwargs('username')
        queryset = PurchaseHistory.objects.filter(username=username)
        return queryset

class ItemPurchaseHistory(generics.ListAPIView):
    serializer_class = PurchaseHistory
    lookup_field = 'item_id'
    # authentication_classes = [IsAdminUser]
    # permission_classes = [IsAdminUser]

    def get_queryset(self):
        item_id = self.kwargs('item_id')
        queryset = PurchaseHistory.objects.filter(item_id_id=item_id)
        return queryset
class RegisterView(generics.CreateAPIView):
    # api_view(['POST'])
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    authentication_classes = []
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        if not isinstance(user, User):
            print(f"Error: Failed to create user. Got type: {type(user)}")  # Debug statement
            return Response({'error': 'Failed to create user.'}, status=status.HTTP_400_BAD_REQUEST)
        # Assuming you want to generate JWT tokens for the user upon registration
        refresh = RefreshToken.for_user(user.id)

        print(f"User created: {user.username}, id: {user.id}")
        print(f"Refresh token: {refresh}")
        return Response({
            'message': str("User created successfully"),
            'user_id': user.id,
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_201_CREATED)

class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        user = authenticate(request, username=username, password=password)
    
    

        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response({'detail': ' Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
