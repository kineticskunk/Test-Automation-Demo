from behave import *

# This should be added to environments.py
# from steps.actionwords import Actionwords
#
# def before_scenario(context, scenario):
#     context.actionwords = Actionwords.new(nil)

use_step_matcher('re')


@given(r'The landing page is open')
def impl(context):
    context.actionwords.the_landing_page_is_open()


@when(r'User clicks the register tab')
def impl(context):
    context.actionwords.user_clicks_the_register_tab()


@when(r'User clicks the cruises tab')
def impl(context):
    context.actionwords.user_clicks_the_cruises_tab()


@then(r'The cruises page is displayed')
def impl(context):
    context.actionwords.the_cruises_page_is_displayed()


@when(r'User clicks the flight tab')
def impl(context):
    context.actionwords.user_clicks_the_flight_tab()

@then(r'The landing page is displayed')
def impl(context):
    context.actionwords.the_landing_page_is_displayed()


@when(r'User clicks the sign-on tab')
def impl(context):
    context.actionwords.user_clicks_the_signon_tab()


@then(r'The sign-on page is displayed')
def impl(context):
    context.actionwords.the_signon_page_is_displayed()


@then(r'The register page is displayed')
def impl(context):
    context.actionwords.the_register_page_is_displayed()


@when(r'User completes form with "(.*)" "(.*)" "(.*)" and "(.*)"')
def impl(context, first_name, last_name, user_name, password):
    context.actionwords.user_completes_form_with_first_name_last_name_user_name_and_password(first_name, last_name, user_name, password)


@when(r'User clicks the register submit button')
def impl(context):
    context.actionwords.user_clicks_the_register_submit_button()


@then(r'The welcome page is displayed with first name "(.*)" last name "(.*)" and user name "(.*)"')
def impl(context, first_name, last_name, user_name):
    context.actionwords.the_welcome_page_is_displayed_with_first_name_first_name_last_name_last_name_and_user_name_user_name(first_name, last_name, user_name)


@then(r'The flights page is displayed')
def impl(context):
    context.actionwords.the_flights_page_is_displayed()


@when(r'User clicks sign-off tab')
def impl(context):
    context.actionwords.user_clicks_signoff_tab()


@when(r'User fills in signs on form with Username "(.*)" and Password "(.*)"')
def impl(context, user_name, password):
    context.actionwords.user_fills_in_signs_on_form_with_username_user_name_and_password_password(user_name, password)


@given(r'User Signs in with Username "(.*)" and Password "(.*)"')
def impl(context, user_name, password):
    context.actionwords.user_signs_in_with_username_user_name_and_password_password(user_name, password)


@when(r'User clicks the login submit form')
def impl(context):
    context.actionwords.user_clicks_the_login_submit_form()


@when(r'User chooses to fly from "(.*)" to "(.*)"')
def impl(context, from_dest, to_dest):
    context.actionwords.user_chooses_to_fly_from_from_dest_to_to_dest(from_dest, to_dest)


@then(r'The select a flight page is displayed')
def impl(context):
    context.actionwords.the_select_a_flight_page_is_displayed()


@when(r'User selects their flight')
def impl(context):
    context.actionwords.user_selects_their_flight()


@then(r'The book a flight page is displayed')
def impl(context):
    context.actionwords.the_book_a_flight_page_is_displayed()


@when(r'User clicks continue after selecting flights')
def impl(context):
    context.actionwords.user_clicks_continue_after_selecting_flights()


@when(r'User clicks continue after entering flight details')
def impl(context):
    context.actionwords.user_clicks_continue_after_entering_flight_details()


@when(r'User fills in passenger and billing details with first name "(.*)" middle name "(.*)" and last name "(.*)"')
def impl(context, first_name, middle_name, last_name):
    context.actionwords.user_fills_in_passenger_and_billing_details_with_first_name_first_name_middle_name_middle_name_and_last_name_last_name(first_name, middle_name, last_name)


@when(r'User clicks secure purchase')
def impl(context):
    context.actionwords.user_clicks_secure_purchase()


@when(r'User chooses to fly on the "(.*)" of "(.*)"')
def impl(context, date, month):
    context.actionwords.user_chooses_to_fly_on_the_date_of_month(date, month)


@when(r'User chooses to return on the "(.*)" of "(.*)"')
def impl(context, date, month):
    context.actionwords.user_chooses_to_return_on_the_date_of_month(date, month)


@then(r'Flight page displays destinations as from "(.*)" to "(.*)"')
def impl(context, from_dest, to_dest):
    context.actionwords.flight_page_displays_destinations_as_from_from_dest_to_to_dest(from_dest, to_dest)


@then(r'Flight page displays the departure date as "(.*)" and the return as "(.*)"')
def impl(context, dep_date, ret_date):
    context.actionwords.flight_page_displays_the_departure_date_as_dep_date_and_the_return_as_ret_date(dep_date, ret_date)


@when(r'User checks Ticketless Travel and Same as billing address checkboxes')
def impl(context):
    context.actionwords.user_checks_ticketless_travel_and_same_as_billing_address_checkboxes()


@when(r'User signs in from landing page with Username "(.*)" and Password "(.*)"')
def impl(context, user_name, password):
    context.actionwords.user_signs_in_from_landing_page_with_username_user_name_and_password_password(user_name, password)


@then(r'The confirmation page is displayed with "(.*)" paying the bill')
def impl(context, bill_payer):
    context.actionwords.the_confirmation_page_is_displayed_with_bill_payer_paying_the_bill(bill_payer)


@given(r'The user confirmed their flights')
def impl(context):
    context.actionwords.the_user_confirmed_their_flights()


@then(r'The menu is displayed as "(.*)"')
def impl(context, menu_display):
    context.actionwords.the_menu_is_displayed_as_menu_display(menu_display)


@when(r'User clicks itinerary tab')
def impl(context):
    context.actionwords.user_clicks_itinerary_tab()


@then(r'The itinerary page is displayed')
def impl(context):
    context.actionwords.the_itinerary_page_is_displayed()
