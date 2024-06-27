from rest_framework import serializers
from shop_app.models import Product,Category,Order



class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = '__all__'
        
        # exclude = ['category_name']
    
    
    
class CategorySerializer(serializers.ModelSerializer):
    
    categorylist = ProductSerializer(many=True, read_only=True)
    
    class Meta:
        model = Category
        fields = '__all__'
        


class OrderSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Order
        fields = '__all__'