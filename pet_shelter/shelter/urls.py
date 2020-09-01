from django.urls import path
from . import views


app_name = "shelter"

urlpatterns = [
    path('api/', views.PetView.as_view(), name="pet_api_get_post"),
    path('api/<int:pk>', views.SinglePetView.as_view(), name="pet_api_update"),
]