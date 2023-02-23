from django.urls import path
from . import views


app_name = "sessions_user"

urlpatterns = [
    path("", views.SessionUserView.as_view(), name="index"),
]
