from .api_exception import ApiExceptionError


class NotFoundError(ApiExceptionError):
    """Not found any instance error."""

    def __init__(self, instance: str) -> None:
        self.status_code = 500
        self.instance = instance

    def __str__(self) -> None:
        return f"{self.instance} instance not found"
