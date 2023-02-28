from django.urls import path
from . import views
from django.urls import include
from django.contrib.auth.decorators import login_required

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
    path("create/", views.ContactCreateView.as_view(), name="create"),
    path("update/<int:pk>/", login_required(views.ContactUpdateView.as_view()), name="update"),
    path("delete/<int:pk>/", login_required(views.ContactDeleteView.as_view()), name="delete"),
    path("details/<int:pk>/", views.ContactDetailView.as_view(), name="details"),
]
