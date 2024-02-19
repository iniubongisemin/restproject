from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, exceptions
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer, CreateProductSerializer
# NB: in django rest framework, you can create your views with class based view

# Create your views here.
class AddCategoryEndpoint(APIView): # if you're serializing multiple instances, use the many=True flag
    def get(self, request, *args):
        category = Category.objects.all() # is a query set 
        serializer = CategorySerializer(category, many=True) # the serializer specifies the field that will be given as an output
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = CategorySerializer(data=request.data) # all incoming data in REST api is in request.data 
        if serializer.is_valid():
            serializer.save() # calls the create or update method depending on the request i.e POST - calls the update method; PUT - calls the create method
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # when the check is not validated
    
class ProductEndPoint(APIView):
    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        serializer = CreateProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductDetailEndpoint(APIView):
    def get_object(self, pk):
        try:
            product = Product.objects.get(id=pk)
            return product
        except Product.DoesNotExist:
            raise exceptions.NotFound('product with this id does not exist')

    def get(self, request, *args, **kwargs): # because it's one product that we're trying to get, you don't need to pass many=True!
        product = self.get_object(self.kwargs['product_id'])
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, *args, **kwargs):
        product = Product.get_object(id=self.kwargs['product_id'])
        serializer = CreateProductSerializer(instance=product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, *args, **kwargs):
        product = Product.get_object(id=self.kwargs['product_id'])
        product.delete()
        return Response({'message':'product deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

# class ProductDetailEndpoint(APIView):
#     def get(self, request, product_id): # because it's one product that we're trying to get, you don't need to pass many=True!
#         product = Product.objects.get(id=['product_id'])
#         serializer = ProductSerializer(product)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def put(self, request, *args, **kwargs):
#         product = Product.objects.get(id=['product_id'])
