from django.shortcuts import render
from django.views.generic import ListView
from . import models


class ListAllTechnologies(ListView):
    model = models.TechnologiesList
    template_name = "technologies/index.html"
    context_object_name = "tech_list"
