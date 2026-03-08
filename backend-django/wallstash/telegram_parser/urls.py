from django.urls import path
from . import views

urlpatterns = [
    path("check-parse/", views.ParseView.as_view(), name="check-parse"),
]
