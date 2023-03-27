from django import forms

from apps.middleware_loggers.models import QueryLogger


class MiddlewareByUserForm(forms.ModelForm):
    class Meta:
        model = QueryLogger
        fields = (
            "path",
            "user",
            "session_id",
        )
        widgets = {
            "user": forms.HiddenInput(),
        }
