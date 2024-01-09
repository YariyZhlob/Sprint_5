"""Проверка входа по кнопке «Войти в аккаунт» на главной"""
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from constants import Constants
from locators import Locators


def test_enter_account_main_page():
    driver = webdriver.Chrome()
    driver.get(Constants.URL)

    #Клик по кнопке Войти в аккаунт
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

    #Проверка наличия кнопки Оформить заказ
    assert driver.find_element(*Locators.MAKE_ORDER_BUTTON).text == "Оформить заказ"

    driver.quit()
