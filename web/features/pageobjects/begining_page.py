from selenium.webdriver.common.by import By
from toolium.pageobjects.page_object import PageObject
from toolium.pageelements import *

from features.pageobjects.landing_page import LandingPageObject


class BeginingPageObject(PageObject):
    def init_page_elements(self):
        pass

    def open(self):
        self.driver.get('{}'.format(self.config.get('Test', 'url')))
        return LandingPageObject(self)
