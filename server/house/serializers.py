from rest_framework import serializers
from .models import House


class HouseListSerializers(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = (
            'id',
            'reg_number',
            'area',
            'types',
            'builder'
        )


class HouseSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault)
    class Meta:
        model = House
        fields = '__all__'
