import datetime

from rest_framework import viewsets

from .models import Pet
from .serializers import PetSerializer


class PetViewSet(viewsets.ModelViewSet):

    serializer_class = PetSerializer
    queryset = Pet.objects.filter(deleted_on__exact=None)

    def perform_destroy(self, instance):
        instance.deleted_on = datetime.date.today()
        instance.save()
