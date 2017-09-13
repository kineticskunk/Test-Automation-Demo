from selenium.webdriver.common.by import By
from toolium.pageobjects.page_object import PageObject
from toolium.pageelements import *


class CruisesPageObject(PageObject):
    def init_page_elements(self):
        pass

    def click_flights(self):
        self.menu = Link(By.XPATH, '/html/body/div/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td[2]/a')
        self.menu.click()    
        return FlightsPageObject(self.driver_wrapper)                 

    def get_title (self):
        self.title = self.driver.title
        return self.title 
        
    def get_menu_text (self):
        self.menu_text = Text(By.XPATH, '/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[2]/td')
        return self.menu_text.text


from pageobjects.flights_page import FlightsPageObject