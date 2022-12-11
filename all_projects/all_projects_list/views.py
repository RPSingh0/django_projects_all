from django.shortcuts import render
from django.views.generic import ListView
from . import models


class ListAllProjects(ListView):
    """
    This class list out all the projects made by me\n
    All the code regarding the same can be found on [Github](https://github.com/RPSingh0/django_projects_all)"""
    model = models.ProjectList
    template_name = "all_projects_list/index.html"
    context_object_name = "project_list"
