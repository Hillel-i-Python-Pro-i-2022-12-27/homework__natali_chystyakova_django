from django.urls import path
from apps.first_example import views
from django.urls import include

app_name = "first_example"

urlpatterns = [
    path(
        "hello",
        include(
            [
                path("", views.GreetingsView.as_view(), name="index"),
                path("<str:name>/<int:age>/", views.GreetingsView.as_view(), name="hello_with_args"),
            ]
        ),
    ),
    path(
        "users",
        include(
            [
                path("", views.UsersView.as_view(), name="users"),
                path("<int:amount>/", views.UsersView.as_view(), name="users"),
            ]
        ),
    ),
]
