import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def driver():
    chrome_driver = webdriver.Chrome()  # Создание экземпляра Chrome WebDriver
    yield chrome_driver

    chrome_driver.quit()  # Закрытие браузера после завершения теста
