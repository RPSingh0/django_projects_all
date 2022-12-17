from django.views.generic import DetailView
from . import models


class ShowUser(DetailView):
    template_name = "user_profile/index.html"
    model = models.UserProfile
    context_object_name = "user"
