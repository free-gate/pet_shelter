from django.urls import path
from . import views


app_name = "shelter"

urlpatterns = [
    path('shelter/', views.PetView.as_view()),
    path('shelter/<int:pk>', views.PetView.as_view()),
]