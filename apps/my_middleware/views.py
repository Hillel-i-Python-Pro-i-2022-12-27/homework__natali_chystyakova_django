from django.views.generic import ListView
from django.db.models import Count
from apps.my_middleware.models import Middleware_my_logger
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

User = get_user_model()


class MiddlewareListView(ListView):
    paginate_by = 5
    model = Middleware_my_logger
    template_name = "middleware/list_middleware.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queries_annotate_all = Middleware_my_logger.objects.all().annotate(count=Count("id"))
        count_all_logs = Middleware_my_logger.objects.count()

        objects_per_page = self.paginate_by
        queryset = queries_annotate_all.order_by("visit_time")
        paginator = Paginator(queryset, objects_per_page)
        page = self.request.GET.get("page")
        try:
            paginated_queryset = paginator.page(page)
        except PageNotAnInteger:
            paginated_queryset = paginator.page(1)
        except EmptyPage:
            paginated_queryset = paginator.page(paginator.num_pages)

        context["title"] = "Logs List"
        context["count_all_logs"] = count_all_logs
        context["queries_annotate_all"] = queries_annotate_all
        context["paginated_queryset"] = paginated_queryset
        return context


class MiddlewareUserListView(ListView):
    paginate_by = 5
    model = Middleware_my_logger
    template_name = "middleware/list_middleware_user.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        users = self.request.user.id
        queries_annotate = Middleware_my_logger.objects.filter(user=users).annotate(count=Count("id"))
        count_logs_by_user = Middleware_my_logger.objects.filter(user=users).count()

        objects_per_page = self.paginate_by
        queryset = queries_annotate.order_by("visit_time")
        paginator = Paginator(queryset, objects_per_page)
        page = self.request.GET.get("page")

        try:
            paginated_queryset = paginator.page(page)
        except PageNotAnInteger:
            paginated_queryset = paginator.page(1)
        except EmptyPage:
            paginated_queryset = paginator.page(paginator.num_pages)

        context["count_logs_by_user"] = count_logs_by_user
        context["queries_annotate"] = queries_annotate
        context["paginated_queryset"] = paginated_queryset
        return context


class MiddlewareSessionsListView(ListView):
    paginate_by = 5
    model = Middleware_my_logger
    template_name = "middleware/list_middleware_sessions.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        session_id = self.request.session.session_key

        queries_annotate = Middleware_my_logger.objects.filter(session_id=session_id).annotate(count=Count("id"))
        count_logs_by_sessions = Middleware_my_logger.objects.filter(session_id=session_id).count()

        objects_per_page = self.paginate_by
        queryset = queries_annotate.order_by("visit_time")
        paginator = Paginator(queryset, objects_per_page)
        page = self.request.GET.get("page")

        try:
            paginated_queryset = paginator.page(page)
        except PageNotAnInteger:
            paginated_queryset = paginator.page(1)
        except EmptyPage:
            paginated_queryset = paginator.page(paginator.num_pages)

        context["count_logs_by_sessions"] = count_logs_by_sessions
        context["queries_annotate"] = queries_annotate
        context["paginated_queryset"] = paginated_queryset
        return context
