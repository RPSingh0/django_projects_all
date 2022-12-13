from django.urls import path
from . import views

urlpatterns = [
    path("", view=views.ListAllProjects.as_view(), name="list-all-projects"),
    path("add_project", view=views.AddNewProject.as_view(),
         name="add-new-project")
]
