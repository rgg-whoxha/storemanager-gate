class UserAlreadyExistsError(Exception):
    """Raised when attempting to create a user that already exists."""
    def __init__(self, username: str):
        self.username = username
        super().__init__(f"User '{username}' already exists")


class UserNotFoundError(Exception):
    """Raised when a user is not found."""
    def __init__(self, username: str):
        self.username = username
        super().__init__(f"User '{username}' not found")
