import logging
from typing import ClassVar
from collections.abc import Callable
from apps.my_middleware.models import Middleware_my_logger


class RequestMiddleware:
    _NAME: ClassVar[str] = "first"

    def __init__(self, get_response: Callable):
        self.get_response = get_response

        self.logger = logging.getLogger("django")
        self.logger.info(f"Init {self._NAME}")

    def __call__(self, request, *args, **kwargs):

        path = request.path

        session_id = request.session.session_key
        if session_id is None:
            request.session.save()
            session_id = request.session.session_key

        user_is_authenticated = request.user.is_authenticated
        user = request.user if user_is_authenticated else request.user.id

        if Middleware_my_logger.objects.filter(
            path=path,
            session_id=session_id,
            user_is_authenticated=user_is_authenticated,
            user=user,
        ).exists():
            is_present = Middleware_my_logger.objects.get(
                path=path,
                session_id=session_id,
                user_is_authenticated=user_is_authenticated,
                user=user,
            )
            is_present.count_requests += 1
            is_present.save()

        else:
            Middleware_my_logger.objects.create(
                path=path,
                session_id=session_id,
                user_is_authenticated=user_is_authenticated,
                user=user,
                count_requests=1,
            )

        message = f"[{self._NAME}]  {path} {user_is_authenticated} {user} {session_id}"
        self.logger.info(f"Before {message}")

        response = self.get_response(request, *args, **kwargs)
        message = f"[{self._NAME}]  {path} {user_is_authenticated} {user} {session_id}"
        self.logger.info(f"After {message}")

        return response
