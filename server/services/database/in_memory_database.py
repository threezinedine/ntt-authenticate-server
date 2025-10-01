import os
from models.user import User
from .database import Database
import sqlite3

class InMemoryDatabase(Database):
    URL = "./test_db.sqlite"

    def __init__(self) -> None:
        super().__init__()
        self.connection: sqlite3.Connection | None = None
        self.cursor: sqlite3.Cursor | None = None

    @staticmethod
    def Setup() -> None:
        """
        Setup the database schema.
        """
        connection = sqlite3.connect(InMemoryDatabase.URL)
        cursor = connection.cursor()

        cursor.execute(
            """
            CREATE TABLE users (
                id TEXT PRIMARY KEY,
                username TEXT NOT NULL,
                password TEXT NOT NULL
            )
            """
        )

        connection.commit()
        connection.close()

    @staticmethod
    def Teardown() -> None:
        """
        Teardown the database schema.
        """
        os.remove(InMemoryDatabase.URL)

    def _ConnectImpl(self) -> None:
        assert self.connection is None, "Database already connected."
        assert self.cursor is None, "Database cursor already initialized."

        self.connection = sqlite3.connect(InMemoryDatabase.URL)
        self.cursor = self.connection.cursor()

    def _DisconnectImpl(self) -> None:
        assert self.connection is not None, "Database not connected."
        assert self.cursor is not None, "Database cursor not initialized."

        self.cursor.close()
        self.connection.close()

        self.cursor = None
        self.connection = None

    # ====================== CRUD Operations ======================
    def CreateUser(self, user: User) -> None:
        assert self.connection is not None, "Database not connected."
        assert self.cursor is not None, "Database cursor not initialized."

        self.cursor.execute(
            "INSERT INTO users (id, username, password) VALUES (?, ?, ?)",
            (user.id, user.username, user.passwordHash),
        )
        self.connection.commit()

    def GetUserByUsername(self, username: str) -> User | None:
        assert self.connection is not None, "Database not connected."
        assert self.cursor is not None, "Database cursor not initialized."

        self.cursor.execute(
            "SELECT id, username, password FROM users WHERE username = ?", (username,)
        )
        row = self.cursor.fetchone()
        if row:
            return User(id=row[0], username=row[1], passwordHash=row[2], createdAt=0)
        return None