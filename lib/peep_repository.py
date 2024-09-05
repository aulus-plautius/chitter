from lib.peep import Peep
from lib.user import User


class PeepRepository:
    def __init__(self, connection) -> None:
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * FROM peeps")
        return [
            Peep(row["id"], row["content"], row["name"], row["handle"], row["time"])
            for row in rows
        ]

    def create(self, peep: Peep):
        peep_id = self._connection.execute(
            "INSERT INTO peeps (content, name, handle, time) VALUES (%s,%s,%s,%s) RETURNING id",
            [peep.content, peep.name, peep.handle, peep.time],
        )[0]["id"]
        if peep.tagged_users:
            for tagged_user in peep.tagged_users:
                user_id = self._connection.execute(
                    "SELECT id FROM users WHERE handle = %s", [tagged_user]
                )[0]["id"]
                self._connection.execute(
                    "INSERT INTO peeps_users VALUES (%s,%s)", [peep_id, user_id] 
                    )
    
    def find(self, peep_id):
        rows = self._connection.execute(
            "SELECT * FROM peeps WHERE id = %s", [peep_id]
        )
        row = rows[0]
        return Peep(row["id"], row["content"], row["name"], row["handle"], row["time"])

    def find_with_users(self, peep_id):
        rows = self._connection.execute(
            "SELECT "
            "peeps_users.peep_id,"
            "peeps_users.user_id, "
            "peeps.content AS peep_content,"
            "peeps.name AS peep_name,"
            "peeps.handle AS peep_handle,"
            "peeps.time AS peep_time,"
            "users.email AS user_email,"
            "users.password AS user_password,"
            "users.name AS user_name,"
            "users.handle AS user_handle "
            "FROM "
            "peeps "
            "JOIN peeps_users ON peeps.id = peeps_users.peep_id "
            "JOIN users ON users.id = peeps_users.user_id "
            "WHERE "
            "peeps.id = %s",
            [peep_id],
        )
        if rows:
            users = [
                User(
                    row["user_id"],
                    row["user_email"],
                    row["user_password"],
                    row["user_name"],
                    row["user_handle"],
                )
                for row in rows
            ]
            return Peep(
                rows[0]["peep_id"],
                rows[0]["peep_content"],
                rows[0]["peep_name"],
                rows[0]["peep_handle"],
                rows[0]["peep_time"],
                users,
            )
        else:
            return self.find(peep_id)

    def all_decending(self, with_tags=False):
        if with_tags:
            peeps = self.all()
            peeps = sorted(peeps, key=lambda peep: peep.time, reverse=True)
            return [self.find_with_users(peep.id) for peep in peeps]
        else:
            peeps = self.all()
            return sorted(peeps, key=lambda peep: peep.time, reverse=True)
    