from selenium.webdriver.common.by import By

from toolium.pageobjects.page_object import PageObject
from toolium.pageelements import *


class BookAFlightPageObject(PageObject):

    def init_page_elements(self):
        pass

    def get_title (self):
        self.title = self.driver.title
        return self.title

    def click_secure_purchase(self):
        self.menu = Link(By.NAME, 'buyFlights')
        self.menu.click()
        return ConfirmationPageObject(self.driver_wrapper)

    def fill_billing_form(self, first_name, middle_name, last_name):

        self.inputElement = self.driver.find_element_by_name('cc_frst_name')
        self.inputElement.send_keys(first_name)

        self.inputElement = self.driver.find_element_by_name('cc_last_name')
        self.inputElement.send_keys(last_name)

        self.inputElement = self.driver.find_element_by_name('cc_mid_name')
        self.inputElement.send_keys(middle_name)

        #Extra Information
        self.inputElement = self.driver.find_element_by_name('passFirst0')
        self.inputElement.send_keys(first_name)

        self.inputElement = self.driver.find_element_by_name('passLast0')
        self.inputElement.send_keys(last_name)

        self.inputElement = self.driver.find_element_by_name('creditnumber')
        self.inputElement.send_keys('8081029283813927')

        self.inputElement = self.driver.find_element_by_name('billAddress1')
        self.inputElement.clear()
        self.inputElement.send_keys('5 Catlain Road')

        self.inputElement = self.driver.find_element_by_name('billAddress2')
        self.inputElement.send_keys('Wynberg')

        self.inputElement = self.driver.find_element_by_name('billCity')
        self.inputElement.clear()
        self.inputElement.send_keys('Cape Town')

        self.inputElement = self.driver.find_element_by_name('billState')
        self.inputElement.clear()
        self.inputElement.send_keys('Western Province')

        self.inputElement = self.driver.find_element_by_name('billZip')
        self.inputElement.clear()
        self.inputElement.send_keys('7335')


        self.inputElement = self.driver.find_element_by_name('delAddress1')
        self.inputElement.clear()
        self.inputElement.send_keys('5 Catlain Road')

        self.inputElement = self.driver.find_element_by_name('delAddress2')
        self.inputElement.send_keys('Wynberg')

        self.inputElement = self.driver.find_element_by_name('delCity')
        self.inputElement.clear()
        self.inputElement.send_keys('Cape Town')

        self.inputElement = self.driver.find_element_by_name('delState')
        self.inputElement.clear()
        self.inputElement.send_keys('Western Province')

        self.inputElement = self.driver.find_element_by_name('delZip')
        self.inputElement.clear()
        self.inputElement.send_keys('7335')

from pageobjects.confirmation_page import ConfirmationPageObject