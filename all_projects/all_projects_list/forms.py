from django import forms
from . import models


class AddNewProject(forms.ModelForm):
    class Meta:
        model = models.ProjectList
        fields = "__all__"

        labels = {
            "project_name": "Name",
            "project_desc": "Description",
            "project_link": "Link/Url"
        }
