"""Проверка работы перехода к разделу Начинки"""
from selenium import webdriver
from constants import Constants
from locators import Locators


def test_enter_fillings_division():
    driver = webdriver.Chrome()
    driver.get(Constants.URL)

    # Клик по кнопке Начинки
    driver.find_element(*Locators.SAUCES_BUTTON)

    # Поиск раздела Соусы
    assert driver.find_element(*Locators.SAUCES_INSCRIPTION).text == "Соусы"

    driver.quit()
