from lib.user import User
def test_object_constructs():
    user = User(1, 'john.doe@example.com', 'Pass1234!', 'John Doe', '@john_doe')
    assert user.id == 1
    assert user.email == 'john.doe@example.com'
    assert user.password == 'Pass1234!'
    assert user.name == 'John Doe'
    assert user.handle == '@john_doe'

def test_object_is_formatted_as_string():
    user = User(1, 'john.doe@example.com', 'Pass1234!', 'John Doe', '@john_doe')
    assert str(user) == 'User(1, john.doe@example.com, Pass1234!, John Doe, @john_doe)'

def test_two_objects_are_equal():
    user1 = User(1, 'john.doe@example.com', 'Pass1234!', 'John Doe', '@john_doe')
    user2 = User(1, 'john.doe@example.com', 'Pass1234!', 'John Doe', '@john_doe')
    assert user1 == user2

