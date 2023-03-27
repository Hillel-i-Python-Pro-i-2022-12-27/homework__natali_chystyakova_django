from . import views
from django.urls import path


app_name = "middleware_loggers"

urlpatterns = [
    path("", views.MiddlewareListView.as_view(), name="list_middleware"),
    path("list-users/", views.MiddlewareUserListView.as_view(), name="list_middleware_user"),
    path("list-sessions/", views.MiddlewareSessionsListView.as_view(), name="list_middleware_sessions"),
]
