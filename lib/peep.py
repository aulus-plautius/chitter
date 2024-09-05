from datetime import datetime


class Peep:
    def __init__(self, id, content, name, handle, time, tagged_users=None) -> None:
        self.id = id
        self.content = content
        self.name = name
        self.handle = handle
        self.time = time

        self.tagged_users = tagged_users

    def __repr__(self) -> str:
        return f"Peep({self.id}, {self.content}, {self.name}, {self.handle}, {datetime.strftime(self.time, '%Y-%m-%d %H:%M')})"

    def __eq__(self, value: object) -> bool:
        return self.__dict__ == value.__dict__
