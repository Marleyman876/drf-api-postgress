from rest_framework import serializers
from .models import Shoppinglist


class ShoppinglistSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Shoppinglist