"""Проверка работы перехода к разделу Булки
Проверка работы перехода к разделу Соусы
Проверка работы перехода к разделу Начинки"""

from constants import Constants
from locators import Locators


class TestConstructorDivision:
    def test_enter_buns_division(self, driver):
        driver.get(Constants.URL)

        # Поиск раздела Булки
        assert driver.find_element(*Locators.BUNS_INSCRIPTION).text == "Булки"

    def test_enter_sauces_division(self, driver):
        driver.get(Constants.URL)

        # Клик по кнопке Соусы
        driver.find_element(*Locators.SAUCES_BUTTON)

        # Поиск раздела Соусы
        assert driver.find_element(*Locators.SAUCES_INSCRIPTION).text == "Соусы"

    def test_enter_fillings_division(self, driver):
        driver.get(Constants.URL)

        # Клик по кнопке Начинки
        driver.find_element(*Locators.SAUCES_BUTTON)

        # Поиск раздела Соусы
        assert driver.find_element(*Locators.SAUCES_INSCRIPTION).text == "Соусы"
