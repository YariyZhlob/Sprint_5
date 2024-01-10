"""Проверка работы перехода к разделу Булки
Проверка работы перехода к разделу Соусы
Проверка работы перехода к разделу Начинки"""

from constants import Constants
from locators import Locators


class TestConstructorDivision:
    def test_enter_buns_division(self, driver):
        driver.get(Constants.URL)

        # Поиск надписи current в разделе Булки
        assert 'current' in driver.find_element(*Locators.BUNS_CURRENT_INSCRIPTION).get_attribute("class")

    def test_enter_sauces_division(self, driver):
        driver.get(Constants.URL)

        # Клик по кнопке Соусы
        driver.find_element(*Locators.SAUCES_BUTTON).click()

        # Поиск надписи current в разделе Соусы
        assert 'current' in driver.find_element(*Locators.SAUCES_CURRENT_INSCRIPTION).get_attribute("class")

    def test_enter_fillings_division(self, driver):
        driver.get(Constants.URL)

        # Клик по кнопке Начинки
        driver.find_element(*Locators.FILLINGS_BUTTON).click()

        # Поиск надписи current в разделе Начинки
        assert 'current' in driver.find_element(*Locators.FILLINGS_CURRENT_INSCRIPTION).get_attribute("class")
