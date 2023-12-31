from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from constants import Constants
from locators import Locators


def test_wrong_password():
    driver = webdriver.Chrome()
    driver.get(Constants.URL)

    # Клик по кнопке Личный кабинет
    driver.find_element(*Locators.MAIN_PAGE_ENTER_PERSONAL_CABINET).click()

    # Ожидание загрузки страницы
    WebDriverWait(driver, 3).until(EC.url_to_be(Constants.LOGIN_PAGE_URL))

    # Ввод email
    driver.find_element(*Locators.LOGIN_PAGE_EMAIL_ENTER).send_keys(Constants.PERSONAL_EMAIL)

    # Ввод некорректного пароля
    driver.find_element(*Locators.LOGIN_PAGE_PASSWORD_ENTER).send_keys(12345)

    # Клик по кнопке войти
    driver.find_element(*Locators.LOGIN_PAGE_ENTER_BUTTON).click()

    assert driver.find_element(*Locators.WRONG_PASSWORD_INSCRIPTION).text == "Некорректный пароль"
