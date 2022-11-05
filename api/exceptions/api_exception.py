class ApiExceptionError(Exception):
    """Basic Exception for custom errors."""

    def __init__(self) -> None:
        self.status_code = 500

    def __str__(self) -> None:
        raise NotImplementedError()
