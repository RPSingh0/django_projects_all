from django.db import models


class TechnologiesList(models.Model):
    tech_name = models.CharField(max_length=50)
    tech_logo = models.FileField(upload_to='tech_images')

    def __str__(self) -> str:
        return self.tech_name
