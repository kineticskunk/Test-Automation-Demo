from selenium.webdriver.common.by import By

from toolium.pageobjects.page_object import PageObject
from toolium.pageelements import *


class SelectFlightPageObject(PageObject):

    def init_page_elements(self):
        pass

    def get_title (self):
        self.title = self.driver.title
        return self.title

    def click_continue(self):
        self.menu = Link(By.XPATH, '/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/p/input')
        self.menu.click()
        return BookAFlightPageObject(self.driver_wrapper)
        
    def get_destination_dep (self):
        self.destination_dep = Text(By.XPATH, '/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table[1]/tbody/tr[1]/td/table/tbody/tr[2]/td[1]/b/font')
        return self.destination_dep.text

    def get_destination_ret (self):
        self.destination_ret = Text(By.XPATH, '/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table[2]/tbody/tr[1]/td/table/tbody/tr[2]/td[1]/b/font')
        return self.destination_ret.text

    def get_date_ret (self):
        self.date_ret = Text(By.XPATH, '/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table[2]/tbody/tr[1]/td/table/tbody/tr[2]/td[2]/b/font')
        return self.date_ret.text

    def get_date_dep (self):
        self.date_dep = Text(By.XPATH, '/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table[1]/tbody/tr[1]/td/table/tbody/tr[2]/td[2]/b/font')
        return self.date_dep.text

from pageobjects.book_a_flight_page import BookAFlightPageObject