#!/usr/bin/python

from selenium import webdriver
import pytest


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='ru',
                     help="Choose language")

@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption('language')
    print(f'\n######################## lang: {language}')
    options = webdriver.ChromeOptions()
    options.add_experimental_option('prefs', {'intl.accept_languages':language})
    print("\nstart browser for test..")
    browser = webdriver.Chrome(options=options)
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    yield browser
    print("\nquit browser..")
    browser.quit()

