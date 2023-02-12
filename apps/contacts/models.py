from django.db import models
from django.urls import reverse


class Contact(models.Model):
    name = models.CharField(max_length=50)
    phone = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    is_auto_generated = models.BooleanField(default=False)

    def get_url(self):
        return reverse("contacts:details", args=[self.id])

    def __str__(self) -> str:
        return f"{self.name} - {self.phone}"

    __repr__ = __str__
