import datetime

from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Pet
from .serializers import PetSerializer


class PetView(APIView):

    def get(self, request):
        pets = Pet.objects.filter(deleted_on__exact=None)
        serializer = PetSerializer(pets, many=True)

        return Response({"pets": serializer.data})

    def post(self, request):
        pet = request.data.get('pet')
        serializer = PetSerializer(data=pet)

        if serializer.is_valid(raise_exception=True):
            pet_saved = serializer.save()

        return Response({"success": "Pet '{}' created successfully".format(pet_saved.nickname)})

    def put(self, request, pk):
        saved_pet = get_object_or_404(Pet.objects.filter(deleted_on__exact=None), pk=pk)
        data = request.data.get('pet')
        serializer = PetSerializer(instance=saved_pet, data=data, partial=True)

        if serializer.is_valid(raise_exception=True):
            pet_saved = serializer.save()

        return Response({
            "success": "Pet '{}' updated successfully".format(pet_saved.nickname)
        })

    def delete(self, request, pk):
        pet = get_object_or_404(Pet.objects.filter(deleted_on__exact=None), pk=pk)
        nickname = pet.nickname
        pet.deleted_on = datetime.date.today()
        pet.save()
        return Response({
            "message": "Pet {} has been deleted.".format(nickname)
        }, status=204)
