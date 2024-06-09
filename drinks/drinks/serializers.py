from rest_framework import serializers
from .models import Drinks


class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drinks
        feilds = ['id' , 'name' , 'description']
        fields = '__all__'