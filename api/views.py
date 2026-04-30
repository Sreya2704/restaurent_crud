from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Restaurant,Dish
from api.serializers import RestaurantSerializer,DishSerializer
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView

class RestaurantListCreateView(ListAPIView,CreateAPIView):

    serializer_class=RestaurantSerializer
    queryset=Restaurant.objects.all()
    # def get(self,request,*args,**kwargs):
    #     qs=Restaurant.objects.all()
    #     serializer_instance=RestaurantSerializer(qs,many=True)
    #     return Response(data=serializer_instance.data)
    
    # def post(self,request,*args,**kwargs): 
    #     form_data=request.data
    #     serializer_instance=RestaurantSerializer(data=form_data)
    #     if serializer_instance.is_valid():
    #         serializer_instance.save()
    #         return Response(data=serializer_instance.data)
    #     else:
    #         return Response(data=serializer_instance.errors)
        
class RestaurantRetrieveUpdateDeleteView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):

    serializer_class=RestaurantSerializer
    queryset=Restaurant.objects.all()

    # def get(self,request,*args,**kwargs):
    #     id=kwargs.get("pk")
    #     qs=Restaurant.objects.get(id=id)
    #     serializer_instance=RestaurantSerializer(qs)
    #     return Response(data=serializer_instance.data)
    
    # def put(self,request,*args,**kwargs):
    #     id=kwargs.get("pk")
    #     form_data=request.data
    #     restaurant_object=Restaurant.objects.get(id=id)
    #     serializer_instance=RestaurantSerializer(data=form_data,instance=restaurant_object)
    #     if serializer_instance.is_valid():
    #         serializer_instance.save()
    #         return Response(data=serializer_instance.data)
    #     else:
    #         return Response(data=serializer_instance.errors)
    
    # def delete(self,request,*args,**kwargs):
    #     id=kwargs.get("pk")
    #     Restaurant.objects.filter(id=id).delete()
    #     return Response(data={"message":"data deleted"})


class DishCreateView(CreateAPIView):

    serializer_class=DishSerializer
    def perform_create(self, serializer):
        id=self.kwargs.get("pk")
        rest_obj=Restaurant.objects.get(id=id)
        serializer.save(restaurant=rest_obj)



    # def post(self,request,*args,**kwargs):
    #     id=kwargs.get("pk")
    #     restaurant_obj=Restaurant.objects.get(id=id)
    #     form_data=request.data
    #     serializer_instance=DishSerializer(data=form_data)
    #     if serializer_instance.is_valid():
    #         serializer_instance.save(restaurant=restaurant_obj)
    #         return Response(data=serializer_instance.data)
    #     else:
    #         return Response(data=serializer_instance.errors)
        
class DishRetrieveUpdateDeleteView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):
    serializer_class=DishSerializer
    queryset=Dish.objects.all()

    # def get(self,request,*args,**kwargs):
    #     id=kwargs.get("pk")
    #     qs=Dish.objects.get(id=id)
    #     serializer_instance=DishSerializer(qs)
    #     return Response(data=serializer_instance.data)
            
    # def put(self,request,*args,**kwargs):
    #     id=kwargs.get("pk")
    #     dish_obj=Dish.objects.get(id=id)
    #     form_data=request.data
    #     serializer_instance=DishSerializer(data=form_data,instance=dish_obj)
    #     if serializer_instance.is_valid():
    #         serializer_instance.save()
    #         return Response(data=serializer_instance.data)
    #     else:
    #         return Response(data=serializer_instance.errors)

    # def delete(self,request,*args,**kwargs):
    #     id=kwargs.get("pk")
    #     Dish.objects.get(id=id).delete()
    #     return Response(data={"message":"deleted..."})
