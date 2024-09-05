class User:
    def __init__(self, id, email, password, name, handle) -> None:
        self.id = id
        self.email = email
        self.password = password
        self.name = name
        self.handle = handle

    def __repr__(self) -> str:
        return f"User({self.id}, {self.email}, {self.password}, {self.name}, {self.handle})"
    
    def __eq__(self, value: object) -> bool:
        return self.__dict__ == value.__dict__