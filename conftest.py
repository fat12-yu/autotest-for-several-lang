#!/usr/bin/python

from selenium import webdriver
import pytest


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='ru',
                     help="Choose language")

@pytest.fixture(scope="function")
def browser(request):
    lang = request.config.getoption('language')
    print(f'\n######################## lang: {lang}')
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('prefs', {'intl.accept_languages': lang})
    print("\nstart browser for test..")
    browser = webdriver.Chrome(options=chrome_options)
    yield browser
    print("\nquit browser..")
    browser.quit()

