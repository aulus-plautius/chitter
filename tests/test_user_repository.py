from lib.user_repository import UserRepository
from lib.user import User
def test_return_all_records(db_connection):
    db_connection.seed('seeds/peeps_users.sql')
    repo = UserRepository(db_connection)
    users = repo.all()
    assert users == [
        User(1, 'john.doe@example.com', 'Pass1234!', 'John Doe', '@john_doe'), 
        User(2, 'jane.smith@example.com', 'Jane#4567', 'Jane Smith', '@jane_smith'),
        User(3, 'mike.johnson@example.com', 'Mike@7890', 'Mike Johnson', '@mike_j'),
        User(4, 'sarah.davis@example.com', 'Sarah!8765', 'Sarah Davis', '@sarah_d')
    ]

def test_create_new_record(db_connection):
    db_connection.seed('seeds/peeps_users.sql')
    repo = UserRepository(db_connection)
    user = User(None, 'new_user@test.com', 'Test1234!', 'Test Dummy', '@test_dum')
    repo.create(user)
    users = repo.all()
    assert users[-1] == User(5, 'new_user@test.com', 'Test1234!', 'Test Dummy', '@test_dum') 

def test_find_user_by_email(db_connection):
    db_connection.seed('seeds/peeps_users.sql')
    repo = UserRepository(db_connection)
    user = repo.find_by_email('john.doe@example.com')
    assert user == User(1, 'john.doe@example.com', 'Pass1234!', 'John Doe', '@john_doe')
