from django.db import models
from django.urls import reverse


class Operator(models.Model):

    name = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.name}"

    __repr__ = __str__


class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    is_auto_generated = models.BooleanField(default=False)
    operator = models.ForeignKey(
        Operator,
        on_delete=models.CASCADE,
        related_name="contacts",
        max_length=50,
        default=None,
        null=True,
        blank=True,
    )
    avatar = models.ImageField(
        max_length=300,
        upload_to="contacts/contact/avatar/",
        blank=True,
        null=True,
        default=None,
    )

    def get_url(self):
        return reverse("contacts:details", args=[self.id])

    def __str__(self) -> str:
        return f"{self.name} - {self.phone}"

    __repr__ = __str__
