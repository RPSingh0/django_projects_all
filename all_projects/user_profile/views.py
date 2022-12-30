from django.views.generic import DetailView
from . import models
import requests
import helper_functions


class ShowUser(DetailView):
    template_name = "user_profile/index.html"
    model = models.UserProfile
    context_object_name = "user"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # getting the leetcode data
        leetcode_stats = requests.get(
            f"https://leetcode-stats-api.herokuapp.com/{context['user'].leetcode_handle}")
        leetcode_stats = helper_functions.get_leetcode_data_from_response_object(
            leetcode_stats)
        context['leetcode_stats'] = leetcode_stats
        return context
