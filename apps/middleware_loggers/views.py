from django.views.generic import ListView
from django.db.models import Count
from apps.middleware_loggers.models import QueryLogger
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator

from apps.middleware_loggers.tools import pagination_processing, paginate_by_condition

User = get_user_model()


class MiddlewareListView(ListView):
    paginate_by = 5
    model = QueryLogger
    template_name = "middleware/list_middleware.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queries_annotate_all = QueryLogger.objects.all().annotate(count=Count("id"))
        count_all_logs = QueryLogger.objects.count()

        objects_per_page = self.paginate_by
        queryset = queries_annotate_all.order_by("visit_time")
        paginator = Paginator(queryset, objects_per_page)
        page = self.request.GET.get("page")

        paginated_queryset = paginate_by_condition(paginator, page)

        context["title"] = "Logs List"
        context["count_all_logs"] = count_all_logs
        context["queries_annotate_all"] = queries_annotate_all
        context["paginated_queryset"] = paginated_queryset
        context["page_obj"] = paginated_queryset
        return context


class MiddlewareUserListView(ListView):
    paginate_by = 5
    model = QueryLogger
    template_name = "middleware/list_middleware_user.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user = self.request.user.id
        query_filter_users = QueryLogger.objects.filter(user=user)
        queries_annotate = query_filter_users.annotate(count=Count("id"))
        count_logs_by_user = query_filter_users.count()

        paginator, page = pagination_processing(self, queries_annotate)
        paginated_queryset = paginate_by_condition(paginator, page)

        context["count_logs_by_user"] = count_logs_by_user
        context["queries_annotate"] = queries_annotate
        context["paginated_queryset"] = paginated_queryset
        context["page_obj"] = paginated_queryset

        return context


class MiddlewareSessionsListView(ListView):
    paginate_by = 5
    model = QueryLogger
    template_name = "middleware/list_middleware_sessions.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        session_id = self.request.session.session_key
        query_filter_sessions = QueryLogger.objects.filter(session_id=session_id)
        queries_annotate = query_filter_sessions.annotate(count=Count("id"))
        count_logs_by_sessions = query_filter_sessions.count()

        paginator, page = pagination_processing(self, queries_annotate)
        paginated_queryset = paginate_by_condition(paginator, page)

        context["count_logs_by_sessions"] = count_logs_by_sessions
        context["queries_annotate"] = queries_annotate
        context["paginated_queryset"] = paginated_queryset
        context["page_obj"] = paginated_queryset
        return context
