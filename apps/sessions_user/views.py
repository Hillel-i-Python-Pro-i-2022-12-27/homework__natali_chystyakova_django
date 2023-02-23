from typing import Final
from datetime import datetime

from faker import Faker
from django.contrib.sessions.backends.cached_db import SessionStore
from django.views.generic import TemplateView

KEY__COUNT_OF_VISITS: Final[str] = "count_of_visits"
KEY__EXTRA_DATA: Final[str] = "extra_data"
DATA_NOW: [str] = "data_now"


class SessionUserView(TemplateView):
    template_name = "sessions_user/index.html"

    def get_context_data(self, **kwargs):
        session: SessionStore = self.request.session
        count_of_visits = session.get(KEY__COUNT_OF_VISITS, 0)
        count_of_visits += 1
        data_now = str(datetime.now())
        session[KEY__COUNT_OF_VISITS] = count_of_visits
        session[DATA_NOW] = data_now

        try:
            extra_data = session[KEY__EXTRA_DATA]
        except KeyError:
            extra_data = {}
            session[KEY__EXTRA_DATA] = extra_data
        extra_data["user"] = Faker().name()

        try:
            nested_data = extra_data[KEY__EXTRA_DATA]
        except KeyError:
            nested_data = {}
            extra_data[KEY__EXTRA_DATA] = nested_data
        nested_data["user"] = Faker().name()

        context = super().get_context_data(**kwargs)
        context["title"] = "Session user"
        context["session_id"] = session.session_key
        context["count_of_visits"] = count_of_visits
        context["extra_data"] = extra_data
        context["data_now"] = data_now
        return context


# Create your views here.
