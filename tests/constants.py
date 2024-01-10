import random
import string


class Constants:
    URL = "https://stellarburgers.nomoreparties.site/"
    RANDOM_EMAIL = ''.join(random.choices(string.ascii_letters, k=8)) + "@mail.ru"
    RANDOM_NAME = ''.join(random.choices(string.ascii_letters, k=8))
    PASSWORD = 123456
    PERSONAL_EMAIL = "knyazev-4@mail.ru"
    LOGIN_PAGE_URL = "https://stellarburgers.nomoreparties.site/login"
    REGISTRATION_PAGE_URL = "https://stellarburgers.nomoreparties.site/register"
    RECOVER_PASSWORD_PAGE = "https://stellarburgers.nomoreparties.site/forgot-password"
    ACCOUNT_PROFILE_PAGE = "https://stellarburgers.nomoreparties.site/account/profile"
