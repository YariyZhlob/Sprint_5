from selenium.webdriver.common.by import By


class Locators:
    MAIN_PAGE_ENTER_PERSONAL_CABINET = (By.XPATH, "//p[contains(@class, 'AppHeader_header__linkText__3q_va') and text()='Личный Кабинет']")
    PERSONAL_CABINET_EMAIL_ENTER = (By.XPATH, "//input[contains(@class,'text input__textfield text_type_main-default') and @name='name']")
    PERSONAL_CABINET_REGISTER_BUTTON = (By.XPATH, "//a[contains(@class, 'Auth_link__1fOlj') and text()='Зарегистрироваться']")
    REGISTRATION_PAGE_NAME_ENTER = (By.XPATH, "//text()[contains(., 'Имя')]/following::input[@class='text input__textfield text_type_main-default'][1]")
    REGISTRATION_PAGE_EMAIL_ENTER = (By.XPATH, "//text()[contains(., 'Email')]/following::input[@class='text input__textfield text_type_main-default'][1]")
    REGISTRATION_PAGE_PASSWORD_ENTER = (By.XPATH, "//input[@class='text input__textfield text_type_main-default' and @type='password' and @name='Пароль']")
    LOGIN_PAGE_PASSWORD_ENTER = (By.XPATH, '//input[@class="text input__textfield text_type_main-default" and @name="Пароль" and @type="password"]')
    LOGIN_PAGE_EMAIL_ENTER = (By.XPATH, "//text()[contains(., 'Email')]/following::input[@class='text input__textfield text_type_main-default'][1]")
    MAKE_ORDER_BUTTON = (By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg"]')
    REGISTRATION_BUTTON_REGISTRATION_PAGE =(By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa' and text()='Зарегистрироваться']")
    LOGIN_PAGE_ENTER_BUTTON = (By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa" and text()="Войти"]')
    WRONG_PASSWORD_INSCRIPTION = (By.XPATH, "//p[@class='input__error text_type_main-default']")




