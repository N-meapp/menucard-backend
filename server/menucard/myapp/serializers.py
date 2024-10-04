from rest_framework import serializers
from .models import *

class MenuItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu_items
        fields = '__all__'

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class CategoryItemsshowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
