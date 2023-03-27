from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class QueryLogger(models.Model):
    path = models.CharField(max_length=250)
    user_is_authenticated = models.BooleanField(default=False)
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name="users",
        max_length=50,
        default=None,
        null=True,
        blank=True,
    )
    session_id = models.CharField(max_length=100, default=None, null=True, blank=True)
    visit_time = models.DateTimeField(auto_now=True)
    count_requests = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=[
                    "path",
                    "user",
                    "session_id",
                    "user_is_authenticated",
                ],
                name="unique_row",
                violation_error_message=None,
            )
        ]

    def __str__(self) -> str:
        return f"{self.path} - {self.user}"

    __repr__ = __str__
