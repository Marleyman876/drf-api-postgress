from rest_framework import generics
from .serializers import ShoppinglistSerializer
from .models import Shoppinglist
from .permissions import IsOwnerOrReadOnly

class ShoppinglistList(generics.ListCreateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Shoppinglist.objects.all()
    serializer_class = ShoppinglistSerializer

class ShoppinglistDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Shoppinglist.objects.all()
    serializer_class = ShoppinglistSerializer
