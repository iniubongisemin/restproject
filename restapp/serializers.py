from rest_framework import serializers, exceptions
from .models import Category, Product

class CategorySerializer(serializers.Serializer): # the Serializer is a class from the serializers module 
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50, min_length=4)

    # fields = ['id', 'name']

    # you can set attributes to read_only=True, write_only=True
    def validate(self, attrs):
        name = attrs.get('name')
        if name == 'acid':
            raise exceptions.ValidationError('please acid is not an accepted category')
        return attrs

    def create(self, validated_data):
        return Category.objects.create(name=validated_data['name'])

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance
    
class ProductSerializer(serializers.ModelSerializer): # by default when you use a ModelSerializer, it already has the create and update method implemented
    class Meta:
        model = Product
        fields = ['id', 'product_name', 'desc', 'price', 'discount_price', 'product_image', 'category', 'production_date', 'expiry_date', 'ratings']

class CreateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'product_name', 'desc', 'price', 'discount_price', 'product_image', 'category', 'production_date', 'expiry_date', 'ratings']