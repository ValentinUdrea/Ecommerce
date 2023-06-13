from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Product

# Here we create a serializer

class ProductSerializer(serializers.ModelSerializer): # This is my serializer -> it turns my product model into JSON format
    class Meta:
        model = Product
        fields = '__all__'

