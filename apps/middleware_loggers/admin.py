from django.contrib import admin
from . import models


@admin.register(models.QueryLogger)
class QueryLoggerAdmin(admin.ModelAdmin):
    list_display = (
        "path",
        "user",
        "session_id",
        "count_requests",
    )
    list_filter = ("user",)


class QueryLoggerInline(admin.TabularInline):
    model = models.QueryLogger
