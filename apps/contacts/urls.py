from django.urls import path
from . import views
from django.urls import include

app_name = "contacts"

urlpatterns = [
    path(
        "list/",
        include(
            [
                path("by-function/", views.list_contacts, name="list_by_function"),
                path("by-class/", views.ContactListView.as_view(), name="list_by_class"),
            ]
        ),
    ),
]
