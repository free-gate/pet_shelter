from rest_framework import serializers

from .models import Pet


class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ('id', 'nickname', 'age', 'date_of_arrival', 'weight_kg', 'height_cm', 'special_sign')
