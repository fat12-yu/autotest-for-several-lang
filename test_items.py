#!/usr/bin/python

import pytest
import time
from selenium.common.exceptions import NoSuchElementException

link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'

class TestUrl():
    def test_url(self, browser):
        browser.get(link)
        try:
            browser.find_element_by_css_selector('button.btn-add-to-basket')
        except:
            assert False, 'Button not found'
