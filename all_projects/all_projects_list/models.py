from django.db import models
from user_profile import models as user_models
from technologies import models as tech_models


class ProjectList(models.Model):
    project_name = models.CharField(max_length=50)
    project_desc = models.CharField(max_length=250)
    project_link = models.CharField(max_length=250, null=True, blank=True)

    belongs_to = models.ForeignKey(
        to=user_models.UserProfile, null=True, blank=True, on_delete=models.SET_NULL)

    technologies_used = models.ManyToManyField(to=tech_models.TechnologiesList)

    def __str__(self) -> str:
        return self.project_name
