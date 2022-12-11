from django.contrib import admin
from . import models


class ProjectListAdmin(admin.ModelAdmin):
    list_display = ("project_name", "project_desc")


admin.site.register(models.ProjectList, ProjectListAdmin)
