from typing import Final
from datetime import datetime


from django.contrib.sessions.backends.cached_db import SessionStore
from django.views.generic import TemplateView

KEY__COUNT_OF_VISITS: Final[str] = "count_of_visits"
# KEY__EXTRA_DATA: Final[str] = "extra_data"
DATA_NOW: [str] = "data_now"
NESTED_TIME: [str] = "nested_time"


class SessionUserView(TemplateView):
    template_name = "sessions_user/index.html"

    def get_context_data(self, **kwargs):
        session: SessionStore = self.request.session
        count_of_visits = session.get(KEY__COUNT_OF_VISITS, 0)

        count_of_visits += 1
        data_now = str(datetime.now())
        nested_time = session.get(NESTED_TIME, 0)
        session[NESTED_TIME] = nested_time
        session[NESTED_TIME] = data_now

        session[KEY__COUNT_OF_VISITS] = count_of_visits

        context = super().get_context_data(**kwargs)
        context["title"] = "Session user"
        context["session_id"] = session.session_key
        context["count_of_visits"] = count_of_visits

        context["data_now"] = data_now
        context["nested_time"] = nested_time

        return context
