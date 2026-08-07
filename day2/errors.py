class AppError(Exception):
    """Base class for all application-specific errors."""
    def __init__(self, message: str, code: int = 500):
        super().__init__(message)
        self.message = message
        self.code = code

    def __str__(self) -> str:
        return f"[Error {self.code}] {self.message}"

class ValidationError(AppError):
    """Raised when input validation fails."""
    def __init__(self, message: str):
        super().__init__(message, code = 400)

class ResourceNotFoundError(AppError):
    """Raised when a requested resource is not found."""
    def __init__(self, resource_name: str, resource_id: str):
        msg = f"Could not find {resource_name} with ID {resource_id}"
        super().__init__(msg, code = 404)

class UnAuthorizedError(AppError):
    """Raised when a user is not authorized to perform an action."""
    def __init__(self, message: str = "Access Denied"):
        super().__init__(message, 401)