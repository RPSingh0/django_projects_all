from django.db import models


class ProjectList(models.Model):
    project_name = models.CharField(max_length=50)
    project_desc = models.CharField(max_length=250)
    project_link = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self) -> str:
        return self.project_name
