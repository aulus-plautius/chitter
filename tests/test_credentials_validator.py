from lib.credentials_validator import CredentialsValidator
def test_correct_email_returns_true():
    validator = CredentialsValidator()
    assert validator.check_email('new_user@test.com')

def test_correct_email_with_no_at_returns_false():
    validator = CredentialsValidator()
    assert not validator.check_email('new_usertest.com')

def test_correct_email_with_2_ats_returns_false():
    validator = CredentialsValidator()
    assert not validator.check_email('new_@user@test.com')

def test_correct_email_with_no_dots_returns_false():
    validator = CredentialsValidator()
    assert not validator.check_email('new_user@testcom')

def test_valid_password_returns_true():
    validator = CredentialsValidator()
    assert validator.check_password("@PassWord")

def test_invalid_password_returns_false():
    validator = CredentialsValidator()
    assert not validator.check_password("@Pass")