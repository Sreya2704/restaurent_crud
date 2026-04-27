from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Restaurant
from api.serializers import RestaurantSerializer

class RestaurantListCreateView(APIView):
    def get(self,request,*args,**kwargs):
        qs=Restaurant.objects.all()
        serializer_instance=RestaurantSerializer(qs,many=True)
        return Response(data=serializer_instance.data)
    
    def post(self,request,*args,**kwargs):
        form_data=request.data
        serializer_instance=RestaurantSerializer(data=form_data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)
        
class RestaurantRetrieveUpdateDeleteView(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Restaurant.objects.get(id=id)
        serializer_instance=RestaurantSerializer(qs)
        return Response(data=serializer_instance.data)
    
    def put(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        form_data=request.data
        restaurant_object=Restaurant.objects.get(id=id)
        serializer_instance=RestaurantSerializer(data=form_data,instance=restaurant_object)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)
    
    def delete(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Restaurant.objects.filter(id=id).delete()
        return Response(data={"message":"data deleted"})
