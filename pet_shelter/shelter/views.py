import datetime

from rest_framework import permissions, viewsets

from .models import Pet
from .permissions import AccessPermission
from .serializers import PetSerializer


class PetApiViewSet(viewsets.ModelViewSet):
    serializer_class = PetSerializer
    permission_classes = (permissions.IsAuthenticated,
                          AccessPermission,)

    def perform_destroy(self, instance):
        instance.deleted_on = datetime.date.today()
        instance.save()

    def get_queryset(self):
        user = self.request.user
        return Pet.objects.filter(deleted_on__exact=None).filter(owner__exact=user)
