import datetime

from rest_framework import serializers

from .models import Pet


class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ('id', 'nickname', 'age', 'date_of_arrival', 'weight_kg', 'height_cm', 'special_sign')

    # nickname = serializers.CharField(max_length=100)
    # age = serializers.IntegerField()
    # date_of_arrival = serializers.DateField(default=datetime.date.today())
    # weight_kg = serializers.FloatField()
    # height_cm = serializers.FloatField()
    # special_sign = serializers.CharField()
    #
    # def create(self, validated_data):
    #     return Pet.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.nickname = validated_data.get('nickname', instance.nickname)
    #     instance.age = validated_data.get('age', instance.age)
    #     instance.date_of_arrival = validated_data.get('date_of_arrival', instance.date_of_arrival)
    #     instance.weight_kg = validated_data.get('weight_kg', instance.weight_kg)
    #     instance.height_cm = validated_data.get('height_cm', instance.height_cm)
    #     instance.special_sign = validated_data.get('special_sign', instance.special_sign)
    #     instance.save()
    #     return instance

