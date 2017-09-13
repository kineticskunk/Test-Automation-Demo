# encoding: UTF-8
from time import sleep
from pageobjects.landing_page import LandingPageObject

class Actionwords:
    def __init__(self):
        pass

    def the_landing_page_is_open(self):
        self.current_page = LandingPageObject()
        self.current_page.open()

    def user_clicks_the_register_tab(self):
        self.current_page = self.current_page.click_register()

    def user_clicks_the_cruises_tab(self):
        self.current_page = self.current_page.click_cruises()

    def the_cruises_page_is_displayed(self):
        assert "Cruises: Mercury Tours" in self.current_page.get_title()

    def user_clicks_the_flight_tab(self):
        self.current_page = self.current_page.click_flights()

    def the_landing_page_is_displayed(self):
        assert "Welcome: Mercury Tours" in self.current_page.get_title()

    def user_clicks_the_signon_tab(self):
        self.current_page = self.current_page.click_signon()

    def the_signon_page_is_displayed(self):
        assert "Sign-on: Mercury Tours" in self.current_page.get_title()

    def the_register_page_is_displayed(self):
        assert "Register: Mercury Tours" in self.current_page.get_title()

    def user_completes_form_with_first_name_last_name_user_name_and_password(self, first_name, last_name, user_name, password):
        self.current_page.fill_in_register_form(first_name, last_name, user_name, password)

    def user_clicks_the_register_submit_button(self):
        self.current_page = self.current_page.register_submit()

    def the_welcome_page_is_displayed_with_first_name_first_name_last_name_last_name_and_user_name_user_name(self, first_name, last_name, user_name):
        fullsentance = 'Dear '+first_name+' '+last_name+','
        assert fullsentance in self.current_page.get_fullName()
        sleep(5)

    def the_flights_page_is_displayed(self):
        assert "Find a Flight: Mercury Tours:" in self.current_page.get_title()

    def user_clicks_signoff_tab(self):
        self.current_page = self.current_page.click_signoff()

    def user_fills_in_signs_on_form_with_username_user_name_and_password_password(self, user_name, password):
        self.current_page.fill_in_login_form(user_name,password)

    def user_signs_in_with_username_user_name_and_password_password(self, user_name, password):
        # When User clicks the sign-on tab
        self.user_clicks_the_signon_tab()
        # Then The sign-on page is displayed
        self.the_signon_page_is_displayed()
        # When User fills in signs on form with Username "userName" and Password "password"
        self.user_fills_in_signs_on_form_with_username_user_name_and_password_password(user_name, password)
        # And User clicks the login submit form
        self.user_clicks_the_login_submit_form()
        # Then The flights page is displayed
        self.the_flights_page_is_displayed()

    def user_clicks_the_login_submit_form(self):
        self.current_page = self.current_page.login_submit()

    def user_chooses_to_fly_from_from_dest_to_to_dest(self, from_dest, to_dest):
        self.current_page.select_destination(from_dest, to_dest)

    def the_select_a_flight_page_is_displayed(self):
        assert "Select a Flight: Mercury Tours" in self.current_page.get_title()

    def user_selects_their_flight(self):
        pass

    def the_book_a_flight_page_is_displayed(self):
        assert "Book a Flight: Mercury Tours" in self.current_page.get_title()

    def user_clicks_continue_after_selecting_flights(self):
        self.current_page = self.current_page.click_continue()

    def user_clicks_continue_after_entering_flight_details(self):
        self.current_page = self.current_page.click_continue()

    def user_fills_in_passenger_and_billing_details_with_first_name_first_name_middle_name_middle_name_and_last_name_last_name(self, first_name, middle_name, last_name):
        self.current_page.fill_billing_form(first_name, middle_name, last_name)

    def user_clicks_secure_purchase(self):
        self.current_page = self.current_page.click_secure_purchase()

    def user_chooses_to_fly_on_the_date_of_month(self, date, month):
        self.current_page.select_dep_date(date, month)

    def user_chooses_to_return_on_the_date_of_month(self, date, month):
        self.current_page.select_ret_date(date, month)

    def user_chooses_their_class_as_service_class(self, service_class):
        pass

    def flight_page_displays_destinations_as_from_from_dest_to_to_dest(self, from_dest, to_dest):
        fullsentance = from_dest+' to '+to_dest
        assert fullsentance in self.current_page.get_destination_dep()
        fullsentance = to_dest+' to '+from_dest
        assert fullsentance in self.current_page.get_destination_ret()

    def flight_page_displays_the_departure_date_as_dep_date_and_the_return_as_ret_date(self, dep_date, ret_date):
        assert ret_date in self.current_page.get_date_ret()
        assert dep_date in self.current_page.get_date_dep()
        sleep(5)

    def user_checks_ticketless_travel_and_same_as_billing_address_checkboxes(self):
        pass

    def user_signs_in_from_landing_page_with_username_user_name_and_password_password(self, user_name, password):
        self.current_page.fill_in_login_form(user_name,password)
        self.current_page = self.current_page.login_submit()

    def the_confirmation_page_is_displayed_with_bill_payer_paying_the_bill(self, bill_payer):
        assert "Flight Confirmation: Mercury Tours" in self.current_page.get_title()
        assert bill_payer in self.current_page.get_name_on_bill()
        sleep(5)

    def the_user_confirmed_their_flights(self):
        # Given User Signs in with Username "JohnDoeSkunkDemo" and Password "SkunkDemo123"
        self.user_signs_in_with_username_user_name_and_password_password(user_name = "JohnDoeSkunkDemo", password = "SkunkDemo123")
        # When User chooses to fly from "London" to "Paris"
        self.user_chooses_to_fly_from_from_dest_to_to_dest(from_dest = "London", to_dest = "Paris")
        # And User chooses to fly on the "5" of "April"
        self.user_chooses_to_fly_on_the_date_of_month(date = "5", month = "April")
        # And User chooses to return on the "7" of "May"
        self.user_chooses_to_return_on_the_date_of_month(date = "7", month = "May")
        # And User clicks continue after entering flight details
        self.user_clicks_continue_after_entering_flight_details()
        # Then The select a flight page is displayed
        self.the_select_a_flight_page_is_displayed()
        # And Flight page displays destinations as from "London" to "Paris"
        self.flight_page_displays_destinations_as_from_from_dest_to_to_dest(from_dest = "London", to_dest = "Paris")
        # And Flight page displays the departure date as "4/5/2017" and the return as "5/7/2017"
        self.flight_page_displays_the_departure_date_as_dep_date_and_the_return_as_ret_date(dep_date = "4/5/2017", ret_date = "5/7/2017")

    def the_menu_is_displayed_as_menu_display(self, menu_display):
        assert menu_display in self.current_page.get_menu_text()

    def user_clicks_itinerary_tab(self):
        self.current_page = self.current_page.click_itinerary()

    def the_itinerary_page_is_displayed(self):
        assert "Select a Flight: Mercury Tours" in self.current_page.get_title()
