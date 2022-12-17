from django.views.generic import DetailView
from . import models


class ShowUser(DetailView):
    template_name = "user_profile/index.html"
    model = models.UserProfile
    context_object_name = "user"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)

    #     # get all the projects made by the user
    #     models.UserProfile
