from django.contrib import admin
from . import models


@admin.register(models.Middleware_my_logger)
class MiddlewareMyLoggerAdmin(admin.ModelAdmin):
    list_display = (
        "path",
        "user",
        "session_id",
        "count_requests",
    )
    list_filter = ("user",)


class MiddlewareMyLoggerInline(admin.TabularInline):
    model = models.Middleware_my_logger
