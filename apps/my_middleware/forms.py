from django import forms

from apps.my_middleware.models import Middleware_my_logger


class MiddlewareByUserForm(forms.ModelForm):
    class Meta:
        model = Middleware_my_logger
        fields = (
            "path",
            "user",
            "session_id",
        )
        widgets = {
            "user": forms.HiddenInput(),
        }
