from django.urls import path
from . import views

urlpatterns = [
    path("technologies", view=views.ListAllTechnologies.as_view())
]
