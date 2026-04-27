from rest_framework import serializers
from api.models import Restaurant

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model=Restaurant
        fields="__all__"
        read_only_fields=["id","is_active","created_at"]
