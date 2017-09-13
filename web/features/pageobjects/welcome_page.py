from selenium.webdriver.common.by import By

from toolium.pageobjects.page_object import PageObject
from toolium.pageelements import *


class WelcomePageObject(PageObject):

    def init_page_elements(self):
        pass

    def get_title (self):
        self.title = self.driver.title
        return self.title

    def get_fullName (self):
        self.fullName = Text(By.XPATH, '/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[3]/td/p[1]/font/b')
        return self.fullName.text
