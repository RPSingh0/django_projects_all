from django.db import models
# Create your models here.


class UserProfile(models.Model):
    user_name = models.CharField(max_length=50)
    professional_email = models.EmailField(max_length=250)
    linkedin_url = models.URLField(null=True, blank=True)
    github_url = models.URLField(null=True, blank=True)
    leetcode_handle = models.CharField(max_length=50, null=True, blank=True)
    hackerrank_handle = models.CharField(max_length=50, null=True, blank=True)
    hackerearth_handle = models.CharField(max_length=50, null=True, blank=True)

    slug = models.SlugField(default="", null=False, db_index=True)

    def __str__(self) -> str:
        string = f"User: {self.user_name}, Email: {self.professional_email}"
        return string
