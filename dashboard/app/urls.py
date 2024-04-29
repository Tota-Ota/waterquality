from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("api/", views.api_dashboard, name="api"),
    path("hw/", views.hw, name="hw")
]