class CredentialsValidator:

    def check_email(self, email: str):
        count_ats = email.count("@")
        count_dots = email.count(".")
        return count_ats == 1 and count_dots > 0
    
    def check_password(self, password: str):
        password_len_check = len(password) > 7
        special_characters = ["!","@","$","%","&"]
        password_character_check = False
        for char in special_characters:
            if char in password:
                password_character_check = True
                break
        return password_len_check and password_character_check
