from django.views.generic import TemplateView

from apps.first_example.services.generate_users import generate_users


class UsersView(TemplateView):

    template_name = "first_example/users.html"

    def get_context_data(self, amount: int = 7, **kwargs) -> dict:
        context_data = super().get_context_data(**kwargs)
        context_data["title"] = "Users"

        context_data["amount"] = amount
        context_data["users"] = generate_users(amount=amount)

        return context_data
