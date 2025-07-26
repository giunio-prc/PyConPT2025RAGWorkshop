from app.interfaces.database import DatabaseI


class FakeDatabase(DatabaseI):
    db: list[str] = []

    def add_text(self, text: str):
        self.db.append(text)

    def get_context(self, question: str) -> list[str]:
        return self.db
