from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from toolium.pageobjects.page_object import PageObject
from toolium.pageelements import *

class FlightsPageObject(PageObject):
    def init_page_elements(self):
        self.select_from = Select(By.NAME, 'fromPort')
        self.select_to = Select(By.NAME,'toPort')
        self.select_from_day = Select(By.NAME, 'fromDay')
        self.select_to_day = Select(By.NAME,'toDay')
        self.select_from_month = Select(By.NAME, 'fromMonth')
        self.select_to_month = Select(By.NAME,'toMonth')
        pass

    def select_ret_date(self, date, month):
        self.select_to_day.option = date
        self.select_to_month.option = month

    def select_dep_date(self, date, month):
        self.select_from_day.option = date
        self.select_from_month.option = month


    def click_signon(self):
        self.menu = Link(By.XPATH, '/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td[1]/a')
        self.menu.click()
        return SignOnPageObject(self.driver_wrapper)

    def click_itinerary(self):
        self.menu = Link(By.XPATH, '/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td[2]/a')
        self.menu.click()
        return ItineraryPageObject(self.driver_wrapper)

    def click_continue(self):
        self.menu = Link(By.XPATH, '/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[14]/td/input')
        self.menu.click()
        return SelectFlightPageObject(self.driver_wrapper)

    def get_title (self):
        self.title = self.driver.title
        return self.title

    def click_signoff(self):
        self.menu = Link(By.XPATH, '/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td[1]/a')
        self.menu.click()
        return SignOnPageObject(self.driver_wrapper)

    def select_destination(self, from_dest, to_dest):

        self.select_from.option = from_dest
        self.select_to.option = to_dest

    def click_cruises(self):
        self.menu = Link(By.XPATH, '/html/body/div/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[5]/td[2]/a')
        self.menu.click()    
        return CruisesPageObject(self.driver_wrapper)

    def get_menu_text (self):
        self.menu_text = Text(By.XPATH, '/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[2]/td')
        return self.menu_text.text

from pageobjects.cruises_page import CruisesPageObject
from pageobjects.sign_on_page import SignOnPageObject
from pageobjects.landing_page import LandingPageObject
from pageobjects.select_flight_page import SelectFlightPageObject
from pageobjects.itinerary_page import ItineraryPageObject



