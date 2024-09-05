from lib.user_repository import UserRepository
from lib.sign_in_authenticator import SignInAuthenticator
def test_valid_email_and_password(db_connection):
    db_connection.seed('seeds/peeps_users.sql')
    repo = UserRepository(db_connection)
    email = 'john.doe@example.com'
    password = 'Pass1234!'
    assert SignInAuthenticator(repo).check_sign_in(email, password) == True

def test_invalid_email_and_password(db_connection):
    db_connection.seed('seeds/peeps_users.sql')
    repo = UserRepository(db_connection)
    email = 'john.doe@eample.com'
    password = 'Pass1234!'
    assert SignInAuthenticator(repo).check_sign_in(email, password) == False

def test_email_and_invalid_password(db_connection):
    db_connection.seed('seeds/peeps_users.sql')
    repo = UserRepository(db_connection)
    email = 'john.doe@example.com'
    password = 'Pass234!'
    assert SignInAuthenticator(repo).check_sign_in(email, password) == False

def test_valid_email_and_valid_password_of_different_account(db_connection):
    db_connection.seed('seeds/peeps_users.sql')
    repo = UserRepository(db_connection)
    email = 'john.doe@example.com'
    password = 'Jane#4567'
    assert SignInAuthenticator(repo).check_sign_in(email, password) == False



