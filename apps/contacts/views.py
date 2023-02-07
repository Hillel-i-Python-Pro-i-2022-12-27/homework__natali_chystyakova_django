from django.views.generic import ListView

from django.shortcuts import render


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
    queryset = Contact.objects.all().order_by("-modified_at")
