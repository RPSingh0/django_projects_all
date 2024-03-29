from django.db import models
from technologies.models import TechnologiesList


class UserProfile(models.Model):
    user_name = models.CharField(max_length=50)
    user_image = models.ImageField(
        upload_to="user_profile_images", null=True, blank=True)
    professional_email = models.EmailField(max_length=250)
    linkedin_handle = models.CharField(max_length=50, null=True, blank=True)
    github_handle = models.CharField(max_length=50, null=True, blank=True)
    leetcode_handle = models.CharField(max_length=50, null=True, blank=True)
    hackerrank_handle = models.CharField(max_length=50, null=True, blank=True)
    hackerearth_handle = models.CharField(max_length=50, null=True, blank=True)

    tech_worked_with = models.ManyToManyField(TechnologiesList, blank=True)

    slug = models.SlugField(default="", null=False, db_index=True)

    def __str__(self) -> str:
        string = f"User: {self.user_name}, Email: {self.professional_email}"
        return string
