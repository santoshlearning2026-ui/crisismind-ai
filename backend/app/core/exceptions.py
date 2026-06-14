"""Application Exceptions."""

from typing import Any, Optional

from fastapi import status


class AppException(Exception):
    """Base application exception."""

    def __init__(
        self,
        detail: str,
        status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR,
        error_code: str = "INTERNAL_SERVER_ERROR",
    ):
        """Initialize exception.
        
        Args:
            detail: Error detail message
            status_code: HTTP status code
            error_code: Application error code
        """
        self.detail = detail
        self.status_code = status_code
        self.error_code = error_code
        super().__init__(self.detail)


class ValidationException(AppException):
    """Validation error."""

    def __init__(self, detail: str):
        super().__init__(
            detail=detail,
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            error_code="VALIDATION_ERROR",
        )


class NotFound(AppException):
    """Resource not found."""

    def __init__(self, detail: str = "Resource not found"):
        super().__init__(
            detail=detail,
            status_code=status.HTTP_404_NOT_FOUND,
            error_code="NOT_FOUND",
        )


class Unauthorized(AppException):
    """Unauthorized access."""

    def __init__(self, detail: str = "Unauthorized"):
        super().__init__(
            detail=detail,
            status_code=status.HTTP_401_UNAUTHORIZED,
            error_code="UNAUTHORIZED",
        )


class Forbidden(AppException):
    """Forbidden access."""

    def __init__(self, detail: str = "Forbidden"):
        super().__init__(
            detail=detail,
            status_code=status.HTTP_403_FORBIDDEN,
            error_code="FORBIDDEN",
        )


class ServiceException(AppException):
    """External service error."""

    def __init__(self, detail: str, error_code: str = "SERVICE_ERROR"):
        super().__init__(
            detail=detail,
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            error_code=error_code,
        )


class TimeoutException(AppException):
    """Operation timeout."""

    def __init__(self, detail: str = "Operation timeout"):
        super().__init__(
            detail=detail,
            status_code=status.HTTP_504_GATEWAY_TIMEOUT,
            error_code="TIMEOUT",
        )
