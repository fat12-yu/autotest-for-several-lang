#!/usr/bin/python

import pytest
import time
from selenium.common.exceptions import NoSuchElementException

link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'

class TestProductForm():
    def test_add_basket_button(self, browser):
        try:
            browser.find_element_by_css_selector('button.btn-add-to-basket')
        except:
            assert False, 'Button add to basket not found'
