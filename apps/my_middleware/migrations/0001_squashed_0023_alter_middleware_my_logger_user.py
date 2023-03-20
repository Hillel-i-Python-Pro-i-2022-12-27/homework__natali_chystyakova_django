# Generated by Django 4.1.5 on 2023-03-20 21:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [
        ("my_middleware", "0001_initial"),
        ("my_middleware", "0002_alter_middleware_my_logger_session_id"),
        ("my_middleware", "0003_middleware_my_logger_unique_row"),
        ("my_middleware", "0004_remove_middleware_my_logger_unique_row_and_more"),
        ("my_middleware", "0005_remove_middleware_my_logger_unique_row_and_more"),
        ("my_middleware", "0006_remove_middleware_my_logger_unique_row_and_more"),
        ("my_middleware", "0007_remove_middleware_my_logger_unique_row_and_more"),
        ("my_middleware", "0008_middleware_my_logger_visit_time"),
        ("my_middleware", "0009_remove_middleware_my_logger_unique_row"),
        ("my_middleware", "0010_middleware_my_logger_unique_row"),
        ("my_middleware", "0011_remove_middleware_my_logger_unique_row"),
        ("my_middleware", "0012_middleware_my_logger_unique_row"),
        ("my_middleware", "0013_alter_middleware_my_logger_session_id"),
        ("my_middleware", "0014_alter_middleware_my_logger_session_id"),
        ("my_middleware", "0015_alter_middleware_my_logger_session_id"),
        ("my_middleware", "0016_alter_middleware_my_logger_session_id"),
        ("my_middleware", "0017_alter_middleware_my_logger_session_id"),
        ("my_middleware", "0018_remove_middleware_my_logger_unique_row"),
        ("my_middleware", "0019_middleware_my_logger_unique_row"),
        ("my_middleware", "0020_alter_middleware_my_logger_count_requests_and_more"),
        ("my_middleware", "0021_alter_middleware_my_logger_user"),
        ("my_middleware", "0022_alter_middleware_my_logger_user"),
        ("my_middleware", "0023_alter_middleware_my_logger_user"),
    ]

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Middleware_my_logger",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("path", models.CharField(max_length=250)),
                ("user_is_authenticated", models.BooleanField(default=False)),
                ("session_id", models.CharField(blank=True, default=None, max_length=100, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                ("count_requests", models.IntegerField(blank=True, default=0)),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        max_length=50,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddConstraint(
            model_name="middleware_my_logger",
            constraint=models.UniqueConstraint(fields=("path", "user", "session_id"), name="unique_row"),
        ),
        migrations.RemoveConstraint(
            model_name="middleware_my_logger",
            name="unique_row",
        ),
        migrations.AddConstraint(
            model_name="middleware_my_logger",
            constraint=models.UniqueConstraint(
                fields=("path", "user", "session_id"), name="unique_row", violation_error_message="repeat"
            ),
        ),
        migrations.RemoveConstraint(
            model_name="middleware_my_logger",
            name="unique_row",
        ),
        migrations.AddConstraint(
            model_name="middleware_my_logger",
            constraint=models.UniqueConstraint(
                fields=("path", "user", "session_id"), name="unique_row", violation_error_message="IntegrityError"
            ),
        ),
        migrations.RemoveConstraint(
            model_name="middleware_my_logger",
            name="unique_row",
        ),
        migrations.AddConstraint(
            model_name="middleware_my_logger",
            constraint=models.UniqueConstraint(
                fields=("path", "user", "session_id", "user_is_authenticated", "created_at", "modified_at"),
                name="unique_row",
            ),
        ),
        migrations.RemoveConstraint(
            model_name="middleware_my_logger",
            name="unique_row",
        ),
        migrations.RemoveField(
            model_name="middleware_my_logger",
            name="created_at",
        ),
        migrations.RemoveField(
            model_name="middleware_my_logger",
            name="modified_at",
        ),
        migrations.AddConstraint(
            model_name="middleware_my_logger",
            constraint=models.UniqueConstraint(
                fields=("path", "user", "session_id", "user_is_authenticated"), name="unique_row"
            ),
        ),
        migrations.AddField(
            model_name="middleware_my_logger",
            name="visit_time",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.RemoveConstraint(
            model_name="middleware_my_logger",
            name="unique_row",
        ),
        migrations.AddConstraint(
            model_name="middleware_my_logger",
            constraint=models.UniqueConstraint(
                fields=("path", "user", "session_id", "user_is_authenticated"), name="unique_row"
            ),
        ),
        migrations.RemoveConstraint(
            model_name="middleware_my_logger",
            name="unique_row",
        ),
        migrations.AddConstraint(
            model_name="middleware_my_logger",
            constraint=models.UniqueConstraint(
                fields=("path", "user", "session_id", "user_is_authenticated"), name="unique_row"
            ),
        ),
        migrations.AlterField(
            model_name="middleware_my_logger",
            name="session_id",
            field=models.CharField(blank=True, default="Unknown user", max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="middleware_my_logger",
            name="session_id",
            field=models.CharField(blank=True, default="AnonymousUser", max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="middleware_my_logger",
            name="session_id",
            field=models.CharField(blank=True, default="Unknown user", max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="middleware_my_logger",
            name="session_id",
            field=models.CharField(blank=True, default="AnonymousUser", max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="middleware_my_logger",
            name="session_id",
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.RemoveConstraint(
            model_name="middleware_my_logger",
            name="unique_row",
        ),
        migrations.AddConstraint(
            model_name="middleware_my_logger",
            constraint=models.UniqueConstraint(
                fields=("path", "user", "session_id", "user_is_authenticated"), name="unique_row"
            ),
        ),
        migrations.AlterField(
            model_name="middleware_my_logger",
            name="count_requests",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="middleware_my_logger",
            name="user",
            field=models.ForeignKey(
                blank=True,
                default=None,
                max_length=50,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="my_middleware",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="middleware_my_logger",
            name="user",
            field=models.ForeignKey(
                blank=True,
                default=None,
                max_length=50,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="user",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="middleware_my_logger",
            name="user",
            field=models.ForeignKey(
                blank=True,
                default=None,
                max_length=50,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="user",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="middleware_my_logger",
            name="user",
            field=models.ForeignKey(
                blank=True,
                default=None,
                max_length=50,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="user",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
