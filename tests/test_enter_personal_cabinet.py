"""Проверка перехода по клику на «Личный кабинет»"""
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from constants import Constants
from locators import Locators

class TestEnterPersonalCabinet:
    def test_enter_personal_cabinet(self,driver):
        driver.get(Constants.URL)

        # Клик по кнопке Личный кабинет
        driver.find_element(*Locators.MAIN_PAGE_ENTER_PERSONAL_CABINET).click()

        # Ожидание загрузки страницы
        WebDriverWait(driver, 3).until(EC.url_to_be(Constants.LOGIN_PAGE_URL))

        # Проверка URL страницы
        assert driver.current_url == Constants.LOGIN_PAGE_URL
