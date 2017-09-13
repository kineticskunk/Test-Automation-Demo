from selenium.webdriver.common.by import By
from toolium.pageobjects.page_object import PageObject
from toolium.pageelements import *


class LandingPageObject(PageObject):
    def init_page_elements(self):
        pass

    def click_register(self):
        self.menu = Link(By.XPATH, "/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td[2]/a")
        self.menu.click()    
        return RegisterPageObject(self.driver_wrapper)                  

    def open(self):
        self.driver.get('{}'.format(self.config.get('Test', 'url')))
        return self

    def get_title (self):
        self.title = self.driver.title
        return self.title

    def click_signon(self):
        self.menu = Link(By.XPATH, '/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td[1]/a')
        self.menu.click()    
        return SignOnPageObject(self.driver_wrapper)

    def fill_in_login_form(self,user_name,password):
        self.inputElement = self.driver.find_element_by_name('userName')
        self.inputElement.send_keys(user_name)

        self.inputElement = self.driver.find_element_by_name('password')
        self.inputElement.send_keys(password)

    def login_submit(self):
        self.submit = Link(By.NAME, 'login')
        self.submit.click()
        return FlightsPageObject(self.driver_wrapper)

    def get_menu_text (self):
        self.menu_text = Text(By.XPATH, '/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[2]/td')
        return self.menu_text.text
        

from pageobjects.register_page import RegisterPageObject
from pageobjects.sign_on_page import SignOnPageObject
from pageobjects.flights_page import FlightsPageObject