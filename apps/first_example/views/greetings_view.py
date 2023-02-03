from django.views.generic import TemplateView


class GreetingsView(TemplateView):

    template_name = "first_example/greetings.html"

    def get_context_data(self, name: str = "Natalina", age: int = 18, **kwargs):

        context_data = super().get_context_data(**kwargs)

        context_data["name"] = name
        context_data["age"] = age

        context_data["title"] = "Greetings"

        return context_data
