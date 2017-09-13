from selenium.webdriver.common.by import By

from toolium.pageobjects.page_object import PageObject
from toolium.pageelements import *


class RegisterPageObject(PageObject):

    def init_page_elements(self):
        self.first_name = self.driver.find_element_by_name('firstName')
        
    def click_cruises(self):
        self.menu = Link(By.XPATH, '/html/body/div/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[5]/td[2]/a')
        self.menu.click()    
        return CruisesPageObject(self.driver_wrapper)

    def get_title (self):
        self.title = self.driver.title
        return self.title

    def fill_in_register_form (self, first_name, last_name, user_name, password ):
        #self.firstname = InputTexts(By.XPATH, '/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[2]/td[2]/input')
        #self.firstname.send_keys('John')
        #if len(self.firstname) > 0:
        self.first_name.send_keys(first_name)

        self.inputElement = self.driver.find_element_by_name('lastName')
        self.inputElement.send_keys(last_name)

        self.inputElement = self.driver.find_element_by_name('phone')
        self.inputElement.send_keys('0823375897')

        self.inputElement = self.driver.find_element_by_name('userName')
        self.inputElement.send_keys(user_name)

        self.inputElement = self.driver.find_element_by_name('address1')
        self.inputElement.send_keys('5 Catlain Road')

        self.inputElement = self.driver.find_element_by_name('address2')
        self.inputElement.send_keys('Wynberg')

        self.inputElement = self.driver.find_element_by_name('city')
        self.inputElement.send_keys('Cape Town')

        self.inputElement = self.driver.find_element_by_name('state')
        self.inputElement.send_keys('Western Province')

        self.inputElement = self.driver.find_element_by_name('postalCode')
        self.inputElement.send_keys('7335')

        self.inputElement = self.driver.find_element_by_name('email')
        self.inputElement.send_keys(user_name)

        self.inputElement = self.driver.find_element_by_name('password')
        self.inputElement.send_keys(password)

        self.inputElement = self.driver.find_element_by_name('confirmPassword')
        self.inputElement.send_keys(password)


    def register_submit(self):
        self.submit = Link(By.XPATH, '/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[18]/td/input')
        self.submit.click()
        return WelcomePageObject(self.driver_wrapper)

from pageobjects.cruises_page import CruisesPageObject
from pageobjects.welcome_page import WelcomePageObject