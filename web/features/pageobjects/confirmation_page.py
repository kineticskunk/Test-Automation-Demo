from selenium.webdriver.common.by import By

from toolium.pageobjects.page_object import PageObject
from toolium.pageelements import *


class ConfirmationPageObject(PageObject):

    def init_page_elements(self):
        pass

    def get_title (self):
        self.title = self.driver.title
        return self.title

    def get_name_on_bill (self):
    	self.billName = Text(By.XPATH, '/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr[1]/td[2]/table/tbody/tr[5]/td/table/tbody/tr[9]/td/p/font[1]')
        return self.billName.text