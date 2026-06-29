import time

from starlette.middleware.base import BaseHTTPMiddleware

from core.logging_config import logger


class RequestLoggingMiddleware(BaseHTTPMiddleware):

    async def dispatch(
        self,
        request,
        call_next,
    ):

        start = time.perf_counter()

        response = await call_next(request)

        logger.info(
            "%s %.4fs",
            request.url.path,
            time.perf_counter() - start,
        )

        return response
