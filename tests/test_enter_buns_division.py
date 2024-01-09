"""Проверка работы перехода к разделу Булки"""
from selenium import webdriver
from constants import Constants
from locators import Locators


def test_enter_buns_division():
    driver = webdriver.Chrome()
    driver.get(Constants.URL)

    #Поиск раздела Булки
    assert driver.find_element(*Locators.BUNS_INSCRIPTION).text == "Булки"

    driver.quit()
