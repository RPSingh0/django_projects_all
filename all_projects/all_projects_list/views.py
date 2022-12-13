from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView
from django.views.generic.edit import FormView
from . import models


class ListAllProjects(ListView):
    """
    This class list out all the projects made by me\n
    All the code regarding the same can be found on [Github](https://github.com/RPSingh0/django_projects_all)"""
    model = models.ProjectList
    template_name = "all_projects_list/index.html"
    context_object_name = "project_list"


class AddNewProject(FormView):
    """
    This class creates a from based on the model: `models.ProjectList`
    """

    form_class = forms.AddNewProject
    template_name = "all_projects_list/add_new_project.html"
#     success_url = reverse("list-all-projects")
