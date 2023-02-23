from django.contrib import admin
from . import models


# admin.site.register(models.Contact)


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "phone",
        "operator",
        "is_auto_generated",
        "created_at",
        "modified_at",
    )
    list_filter = (
        "operator",
        "is_auto_generated",
    )


class ContactInline(admin.TabularInline):
    model = models.Contact


@admin.register(models.Operator)
class OperatorAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "created_at",
        "modified_at",
    )
    # list_filter = ("name",)
    inlines = (ContactInline,)
