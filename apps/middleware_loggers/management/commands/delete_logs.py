import logging

from django.core.management import BaseCommand

from apps.middleware_loggers.models import QueryLogger


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            "--Delete-logs",
            help="Do you want to delete all logs?",
            action="store_true",
        )

    def handle(self, *args, **options):
        logger = logging.getLogger("django")
        queryset = QueryLogger.objects.all()
        logger.info(f"Current number of logs before: {queryset.count()}")
        queryset_for_delete = queryset
        total_deleted, details = queryset_for_delete.delete()
        logger.info(f"Total deleted: {total_deleted}, details: {details}")
        logger.info(f"Current number of logs after deletion: {queryset.count()}")
