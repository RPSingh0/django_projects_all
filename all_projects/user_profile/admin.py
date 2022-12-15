from django.contrib import admin
from . import models


class UserDetailsAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        "slug": ("user_name",)
    }
    list_display = ("user_name",
                    "professional_email")


admin.site.register(models.UserProfile, UserDetailsAdmin)
