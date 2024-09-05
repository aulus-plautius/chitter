class SignInAuthenticator:
    def __init__(self, repository) -> None:
        self._repository = repository

    def check_sign_in(self, input_email, input_password):
        users = self._repository.all()
        emails = [user.email for user in users]
        print(emails)
        if input_email not in emails:
            return False
        password = next(user.password for user in users if user.email == input_email)
        print(password)
        if input_password != password:
            return False
        return True
        
