"""Проверка выхода из аккаунта"""
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from constants import Constants
from locators import Locators


class TestLogoutFromAccount:
    def test_logout_from_account(self, driver):
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

        # Клик по кнопке Личный кабинет
        driver.find_element(*Locators.MAIN_PAGE_ENTER_PERSONAL_CABINET).click()

        # Ожидание загрузки страницы
        WebDriverWait(driver, 3).until(EC.url_to_be(Constants.ACCOUNT_PROFILE_PAGE))

        # Клик по кнопке Выход
        driver.find_element(*Locators.EXIT_BUTTON_PROFILE_PAGE).click()

        # Ожидание загрузки страницы
        WebDriverWait(driver, 3).until(EC.url_to_be(Constants.LOGIN_PAGE_URL))

        # Проверка URL страницы
        assert driver.current_url == Constants.LOGIN_PAGE_URL
