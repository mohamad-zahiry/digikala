from rest_framework import serializers

from .models import Laptop, Mobile


class LaptopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Laptop
        exclude = ("id",)


class MobileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mobile
        exclude = ("id",)
