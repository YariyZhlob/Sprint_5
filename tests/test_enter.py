"""Проверка входа по кнопке «Войти в аккаунт» на главной
Проверка входа через кнопку «Личный кабинет»
Проверка входа через кнопку в форме регистрации
Проверка входа через кнопку в форме восстановления пароля"""

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from constants import Constants
from locators import Locators


class TestEnter:
    def test_enter_account_main_page(self, driver):
        driver.get(Constants.URL)

        # Клик по кнопке Войти в аккаунт
        driver.find_element(*Locators.ENTER_ACCOUNT_MAIN_PAGE).click()

        # Ожидание загрузки страницы
        WebDriverWait(driver, 3).until(EC.url_to_be(Constants.LOGIN_PAGE_URL))

        # Ввод email
        driver.find_element(*Locators.LOGIN_PAGE_EMAIL_ENTER).send_keys(Constants.PERSONAL_EMAIL)

        # Ввод пароля
        driver.find_element(*Locators.LOGIN_PAGE_PASSWORD_ENTER).send_keys(Constants.PASSWORD)

        # Клик по кнопке войти
        driver.find_element(*Locators.LOGIN_PAGE_ENTER_BUTTON).click()

        # Ожидание загрузки страницы
        WebDriverWait(driver, 3).until(EC.url_to_be(Constants.URL))

        # Проверка наличия кнопки Оформить заказ
        assert driver.find_element(*Locators.MAKE_ORDER_BUTTON).text == "Оформить заказ"

    def test_enter_via_personal_cabinet_button(self, driver):
        driver.get(Constants.URL)

        # Клик по кнопке Личный кабинет
        driver.find_element(*Locators.MAIN_PAGE_ENTER_PERSONAL_CABINET).click()

        # Ожидание загрузки страницы
        WebDriverWait(driver, 3).until(EC.url_to_be(Constants.LOGIN_PAGE_URL))

        # Ввод email
        driver.find_element(*Locators.LOGIN_PAGE_EMAIL_ENTER).send_keys(Constants.PERSONAL_EMAIL)

        # Ввод пароля
        driver.find_element(*Locators.LOGIN_PAGE_PASSWORD_ENTER).send_keys(Constants.PASSWORD)

        # Клик по кнопке войти
        driver.find_element(*Locators.LOGIN_PAGE_ENTER_BUTTON).click()

        # Ожидание загрузки страницы
        WebDriverWait(driver, 3).until(EC.url_to_be(Constants.URL))

        # Проверка наличия кнопки Оформить заказ
        assert driver.find_element(*Locators.MAKE_ORDER_BUTTON).text == "Оформить заказ"

    def test_enter_via_registration_page(self, driver):
        driver.get(Constants.URL)

        # Клик по кнопке Личный кабинет
        driver.find_element(*Locators.MAIN_PAGE_ENTER_PERSONAL_CABINET).click()

        # Ожидание загрузки страницы
        WebDriverWait(driver, 3).until(EC.url_to_be(Constants.LOGIN_PAGE_URL))

        # Клик по кнопке Зарегистрироваться
        driver.find_element(*Locators.PERSONAL_CABINET_REGISTER_BUTTON).click()

        # Ожидание загрузки страницы
        WebDriverWait(driver, 3).until(EC.url_to_be(Constants.REGISTRATION_PAGE_URL))

        # Клик по кнопке Войти
        driver.find_element(*Locators.ENTER_BUTTON_REGISTRATION_PAGE).click()

        # Ожидание загрузки страницы
        WebDriverWait(driver, 3).until(EC.url_to_be(Constants.LOGIN_PAGE_URL))

        # Ввод email
        driver.find_element(*Locators.LOGIN_PAGE_EMAIL_ENTER).send_keys(Constants.PERSONAL_EMAIL)

        # Ввод пароля
        driver.find_element(*Locators.LOGIN_PAGE_PASSWORD_ENTER).send_keys(Constants.PASSWORD)

        # Клик по кнопке войти
        driver.find_element(*Locators.LOGIN_PAGE_ENTER_BUTTON).click()

        # Ожидание загрузки страницы
        WebDriverWait(driver, 3).until(EC.url_to_be(Constants.URL))

        # Проверка наличия кнопки Оформить заказ
        assert driver.find_element(*Locators.MAKE_ORDER_BUTTON).text == "Оформить заказ"

    def test_enter_recovery_password(self, driver):
        driver.get(Constants.URL)

        # Клик по кнопке Личный кабинет
        driver.find_element(*Locators.MAIN_PAGE_ENTER_PERSONAL_CABINET).click()

        # Ожидание загрузки страницы
        WebDriverWait(driver, 3).until(EC.url_to_be(Constants.LOGIN_PAGE_URL))

        # Клик по кнопке Восстановить пароль
        driver.find_element(*Locators.RECOVER_BUTTON).click()

        # Ожидание загрузки страницы
        WebDriverWait(driver, 3).until(EC.url_to_be(Constants.RECOVER_PASSWORD_PAGE))

        # Клик по кнопке Войти
        driver.find_element(*Locators.RECOVER_PAGE_ENTER_BUTTON).click()

        # Ожидание загрузки страницы
        WebDriverWait(driver, 3).until(EC.url_to_be(Constants.LOGIN_PAGE_URL))

        # Ввод email
        driver.find_element(*Locators.LOGIN_PAGE_EMAIL_ENTER).send_keys(Constants.PERSONAL_EMAIL)

        # Ввод пароля
        driver.find_element(*Locators.LOGIN_PAGE_PASSWORD_ENTER).send_keys(Constants.PASSWORD)

        # Клик по кнопке войти
        driver.find_element(*Locators.LOGIN_PAGE_ENTER_BUTTON).click()

        # Ожидание загрузки страницы
        WebDriverWait(driver, 3).until(EC.url_to_be(Constants.URL))

        # Проверка наличия кнопки Оформить заказ
        assert driver.find_element(*Locators.MAKE_ORDER_BUTTON).text == "Оформить заказ"
