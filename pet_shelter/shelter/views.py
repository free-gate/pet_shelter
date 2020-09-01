import datetime

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Pet
from .serializers import PetSerializer


class PetView(ListCreateAPIView):
    queryset = Pet.objects.filter(deleted_on__exact=None)
    serializer_class = PetSerializer


class SinglePetView(RetrieveUpdateDestroyAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer

    def perform_destroy(self, instance):
        instance.deleted_on = datetime.date.today()
        instance.save()
