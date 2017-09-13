from selenium.webdriver.common.by import By

from toolium.pageobjects.page_object import PageObject
from toolium.pageelements import *


class ItineraryPageObject(PageObject):

    def init_page_elements(self):
        pass

    def get_title (self):
        self.title = self.driver.title
        return self.title

    def click_signoff(self):
        self.menu = Link(By.XPATH, '/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td[1]/a')
        self.menu.click()
        return SignOnPageObject(self.driver_wrapper)


from pageobjects.sign_on_page import SignOnPageObject
