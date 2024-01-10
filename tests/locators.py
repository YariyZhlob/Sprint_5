from selenium.webdriver.common.by import By


class Locators:
    #Кнопка входа в личный кабинет на главной странице
    MAIN_PAGE_ENTER_PERSONAL_CABINET = (By.XPATH, "//p[contains(@class, 'AppHeader_header__linkText__3q_va') and text()='Личный Кабинет']")
    #Ввод email в личном кабинете
    PERSONAL_CABINET_EMAIL_ENTER = (By.XPATH, "//input[contains(@class,'text input__textfield text_type_main-default') and @name='name']")
    #Кнопка Зарегистрироваться в личном кабинете
    PERSONAL_CABINET_REGISTER_BUTTON = (By.XPATH, "//a[contains(@class, 'Auth_link__1fOlj') and text()='Зарегистрироваться']")
    #Ввод имени в личном кабинете
    REGISTRATION_PAGE_NAME_ENTER = (By.XPATH, "//text()[contains(., 'Имя')]/following::input[@class='text input__textfield text_type_main-default'][1]")
    #Ввод email на странице регистрации
    REGISTRATION_PAGE_EMAIL_ENTER = (By.XPATH, "//text()[contains(., 'Email')]/following::input[@class='text input__textfield text_type_main-default'][1]")
    #Ввод пароля на странице регистрации
    REGISTRATION_PAGE_PASSWORD_ENTER = (By.XPATH, "//input[@class='text input__textfield text_type_main-default' and @type='password' and @name='Пароль']")
    #Ввод пароля на странице логина
    LOGIN_PAGE_PASSWORD_ENTER = (By.XPATH, '//input[@class="text input__textfield text_type_main-default" and @name="Пароль" and @type="password"]')
    #Ввод email на странице логина
    LOGIN_PAGE_EMAIL_ENTER = (By.XPATH, "//text()[contains(., 'Email')]/following::input[@class='text input__textfield text_type_main-default'][1]")
    #Кнопка Оформить заказ
    MAKE_ORDER_BUTTON = (By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg"]')
    #Кнопка зарегистрироваться на странице регистрации
    REGISTRATION_BUTTON_REGISTRATION_PAGE =(By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa' and text()='Зарегистрироваться']")
    #Кнопка войти на странице логина
    LOGIN_PAGE_ENTER_BUTTON = (By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa" and text()="Войти"]')
    #Надпись некорректный пароль
    WRONG_PASSWORD_INSCRIPTION = (By.XPATH, "//p[@class='input__error text_type_main-default']")
    #Войти в аккаунт на главной странице
    ENTER_ACCOUNT_MAIN_PAGE = (By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg' and text()='Войти в аккаунт']")
    #Кнопка войти на странице регистрации
    ENTER_BUTTON_REGISTRATION_PAGE = (By.XPATH, '//a[@class="Auth_link__1fOlj" and text()="Войти"]')
    #Кнопка восстановить пароль
    RECOVER_BUTTON = (By.XPATH, '//a[@class="Auth_link__1fOlj" and text()="Восстановить пароль"]')
    #Кнопка войти на странице воссстановления пароля
    RECOVER_PAGE_ENTER_BUTTON = (By.XPATH, '//a[@class="Auth_link__1fOlj" and text()="Войти"]')
    #Кнопка выйти на странице профиля
    EXIT_BUTTON_PROFILE_PAGE = (By.XPATH, '//button[@class="Account_button__14Yp3 text text_type_main-medium text_color_inactive" and text()="Выход"]')
    #Кнопка Булки
    BUNS_BUTTON = (By.XPATH, '//span[@class="text text_type_main-default" and text()="Булки"]')
    #Надпись Булки
    BUNS_INSCRIPTION = (By.XPATH, '//h2[@class="text text_type_main-medium mb-6 mt-10" and text()="Булки"]')
    #Кнопка Соусы
    SAUCES_BUTTON = (By.XPATH, '//span[@class="text text_type_main-default" and text()="Соусы"]')
    #Надпись Соусы
    SAUCES_INSCRIPTION = (By.XPATH, '//h2[@class="text text_type_main-medium mb-6 mt-10"][2]')
    #Кнопка Начинки
    FILLINGS_BUTTON = (By.XPATH, '//span[@class="text text_type_main-default" and text()="Начинки"]')
    #Надпись Начинки
    FILLINGS_INSCRIPTION = (By.XPATH, '//h2[@class="text text_type_main-medium mb-6 mt-10"][3]')
    #Элемент для надписи Current в разделе Соусы
    SAUCES_CURRENT_INSCRIPTION = (By.XPATH, '//span[@class="text text_type_main-default" and text()="Соусы"]/parent::div')
    #Элемент для надписи Current в разделе Булки
    BUNS_CURRENT_INSCRIPTION = (By.XPATH, '//span[@class="text text_type_main-default" and text()="Булки"]/parent::div')
    #Элемент для надписи Current в разделе Начинки
    FILLINGS_CURRENT_INSCRIPTION = (By.XPATH, '//span[@class="text text_type_main-default" and text()="Начинки"]/parent::div')

