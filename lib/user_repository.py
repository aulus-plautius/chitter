from lib.user import User
class UserRepository:
    def __init__(self, connection) -> None:
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM users')
        return [User(row["id"], 
                    row["email"], 
                    row["password"], 
                    row["name"], 
                    row["handle"]
                    ) for row in rows
            ]
    
    def create(self, user: User):
        self._connection.execute(
            'INSERT INTO users (email, password, name, handle)' \
            'VALUES (%s, %s, %s, %s)',
            [user.email, user.password, user.name, user.handle]
        )

    def find_by_email(self, email):
        rows = self._connection.execute('SELECT * FROM users WHERE email = %s', [email])
        row = rows[0]
        return User(row["id"], row["email"], row["password"], row["name"], row["handle"])
