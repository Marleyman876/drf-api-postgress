from django.urls import path
from .views import ShoppinglistList, ShoppinglistDetail

urlpatterns = [
    path('',ShoppinglistList.as_view(), name='shoppinglist_list'),
    path('<int:pk>/', ShoppinglistDetail.as_view(), name='shoppinglist_detail')
]
