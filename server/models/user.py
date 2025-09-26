from dataclasses import dataclass


@dataclass
class User:
    """
    Represents a user in the system.
    """

    id: str 
    """
    Unique identifier for the user.
    """

    username: str

    passwordHash: str
    """
    Hashed password for the user.
    """

    createdAt: int
    """
    Timestamp when the user was created.
    """