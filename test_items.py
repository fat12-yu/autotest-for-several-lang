#!/usr/bin/python

import pytest
import time
from selenium.common.exceptions import NoSuchElementException

class TestProductForm():
    def test_add_basket_button(self, browser):
        browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
        try:
            button = browser.find_element_by_css_selector('button.btn-add-to-basket')
        except:
            assert False, 'Button add to basket not found'
        assert button.is_displayed(), "Button is not displayed"
