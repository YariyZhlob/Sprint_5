"""Проверка работы перехода к разделу Соусы"""
from selenium import webdriver
from constants import Constants
from locators import Locators


def test_enter_sauces_division():
    driver = webdriver.Chrome()
    driver.get(Constants.URL)

    # Клик по кнопке Соусы
    driver.find_element(*Locators.SAUCES_BUTTON)

    # Поиск раздела Соусы
    assert driver.find_element(*Locators.SAUCES_INSCRIPTION).text == "Соусы"

    driver.quit()
