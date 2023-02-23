from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.shortcuts import render
from django.urls import reverse_lazy

from apps.contacts.models import Contact


def list_contacts(request):
    return render(
        request=request,
        template_name="contacts/contact_list.html",
        context={
            "object_list": Contact.objects.all(),
        },
    )


class ContactListView(ListView):
    model = Contact
    allow_empty = False
    queryset = Contact.objects.all().order_by("-modified_at")


class ContactDetailView(DetailView):
    model = Contact
    pk_url_kwarg = "pk"


class ContactCreateView(CreateView):
    model = Contact
    fields = (
        "name",
        "phone",
        "avatar",
        "operator",
        "is_auto_generated",
    )
    success_url = reverse_lazy("contacts:list_by_class")


class ContactUpdateView(UpdateView):
    model = Contact
    fields = (
        "id",
        "name",
        "phone",
        "avatar",
        "operator",
        "is_auto_generated",
    )
    success_url = reverse_lazy("contacts:list_by_class")


class ContactDeleteView(DeleteView):
    model = Contact

    success_url = reverse_lazy("contacts:list_by_class")
