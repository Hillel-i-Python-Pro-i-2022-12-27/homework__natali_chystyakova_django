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
    name = models.CharField(max_length=50)
    phone = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    is_auto_generated = models.BooleanField(default=False)
    operator = models.ForeignKey(
        Operator,
        on_delete=models.CASCADE,
        related_name="contacts",
        default=None,
        null=True,
        blank=False,
    )

    def get_url(self):
        return reverse("contacts:details", args=[self.id])

    def __str__(self) -> str:
        return f"{self.name} - {self.phone}"

    __repr__ = __str__
