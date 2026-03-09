from django.urls import path
from . import views

urlpatterns = [
    path("parse-channel/", views.ParseView.as_view(), name="parse-channel"),
]
