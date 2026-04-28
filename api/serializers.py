from rest_framework import serializers
from api.models import Restaurant,Dish

class RestaurantSerializer(serializers.ModelSerializer):
    dish_count=serializers.SerializerMethodField(read_only=True)
    dishes=serializers.SerializerMethodField(read_only=True)
    class Meta:
        model=Restaurant
        fields="__all__"
        read_only_fields=["id","is_active","created_at"]
    def get_dish_count(self,obj):
        count=Dish.objects.filter(restaurant=obj).count()
        return count
    def get_dishes(self,obj):
        menu_items=Dish.objects.filter(restaurant=obj)
        serializer_instance=DishSerializer(menu_items,many=True)
        return serializer_instance.data

class DishSerializer(serializers.ModelSerializer):
    restaurant=serializers.StringRelatedField(read_only=True)
    class Meta:
        model=Dish
        fields="__all__"
        read_only_fields=["id","restaurant","is_available","created_at"]