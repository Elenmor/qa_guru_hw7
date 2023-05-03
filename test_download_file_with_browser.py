import time
import os
from selenium import webdriver
from selene import browser
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from os_path_scripts import PROJECT_ROOT_PATH, resources

# TODO оформить в тест, добавить ассерты и использовать универсальный путь к tmp

def test_download_file_with_browser():
    options = webdriver.ChromeOptions()

    prefs = {
        "download.default_directory": PROJECT_ROOT_PATH,
        "download.prompt_for_download": False
    }
    options.add_experimental_option("prefs", prefs)

    browser.config.driver_options = options

    browser.open("https://github.com/pytest-dev/pytest")
    browser.element(".d-none .Button-label").click()
    browser.element('[data-open-app="link"]').click()

    time.sleep(10)

    file_element = os.path.join(PROJECT_ROOT_PATH, 'pytest-main.zip')
    assert os.path.exists(file_element), f"The file {file_element} was not downloaded"

    size_file = os.path.getsize(file_element)
    assert size_file == 1565002