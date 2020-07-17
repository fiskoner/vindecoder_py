from rest_framework import serializers
from vindecoder.models import Car


# class CarSerializer(serializers.Serializer):
#     mark = serializers.CharField()
#     additionalCode = serializers.CharField()
#     manufacturer = serializers.CharField()
#     markOwner = serializers.CharField()
#     countryCode = serializers.CharField()
#     countryName = serializers.CharField()
#     additionalInfo = serializers.CharField()
#     bodyType = serializers.CharField()
#     model = serializers.CharField()
#     engineCapacity = serializers.CharField()
#     engineKW = serializers.CharField()
#     color = serializers.CharField()
#     year = serializers.CharField()

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'
