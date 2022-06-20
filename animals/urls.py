from django.urls import path

from .views import AnimalView, AnimalViewDetail

urlpatterns = [
    path("animals/", AnimalView.as_view()), 
    path("animals/<int:animal_id>", AnimalViewDetail.as_view()),
]
