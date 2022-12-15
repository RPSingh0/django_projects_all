from django.urls import path
from . import views

urlpatterns = [
    path("<slug:slug>", view=views.ShowUser.as_view(), name="show-user")
]
