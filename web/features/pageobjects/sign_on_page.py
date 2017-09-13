from selenium.webdriver.common.by import By
from toolium.pageobjects.page_object import PageObject
from toolium.pageelements import *


class SignOnPageObject(PageObject):
    def init_page_elements(self):
        pass

    def click_home(self):
        self.menu = Link(By.XPATH, '/html/body/div/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td[2]/font/a')
        self.menu.click()    
        return LandingPageObject(self.driver_wrapper)

    def get_title (self):
        self.title = self.driver.title
        return self.title

    def fill_in_login_form(self,user_name,password):
        self.inputElement = self.driver.find_element_by_name('userName')
        self.inputElement.send_keys(user_name)

        self.inputElement = self.driver.find_element_by_name('password')
        self.inputElement.send_keys(password)

    def login_submit(self):
        self.submit = Link(By.XPATH, '/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[4]/td/input')
        self.submit.click()
        return FlightsPageObject(self.driver_wrapper)

from pageobjects.flights_page import FlightsPageObject
from pageobjects.landing_page import LandingPageObject