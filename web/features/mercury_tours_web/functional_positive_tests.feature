@pos
Feature: Functional positive tests
    As a web user
    I want to use the functionality of Mercury Tours

  Background:
    Given The landing page is open

  Scenario Outline: Register with valid details (uid:2c8c9605-9a1c-4a65-be37-47461cfc7fbf)
    # As a web user
    # I would like to create an account on Mercury Tours
    When User clicks the register tab
    And User completes form with "John" "Doe" "JohnDoeSkunkDemo" and "SkunkDemo123"
    And User clicks the register submit button
    Then The welcome page is displayed with first name "John" last name "Doe" and user name "JohnDoeSkunkDemo"

    Examples:
      |  | hiptest-uid |
      |  | uid:5925ea6d-e0bc-434f-a951-57e9693b9554 |

  Scenario: Sign in  with valid details and sign off (uid:2a431087-f8c7-441d-98b3-acbe40d88d3a)
    # As a Mercury Tours user
    # I would like to sign in successfully
    # Add sign off successfully
    Given User Signs in with Username "JohnDoeSkunkDemo" and Password "SkunkDemo123"
    When User clicks sign-off tab
    Then The sign-on page is displayed

  Scenario: Login with valid details from landing page (uid:73a9cbb9-1236-4750-98a9-c4920b5ff402)
    # As a mercury tours user 
    # I would like to sign in from the landing page
    # and validate I am signed in
    When User signs in from landing page with Username "JohnDoeSkunkDemo" and Password "SkunkDemo123"
    Then The flights page is displayed
    When User clicks sign-off tab
    Then The sign-on page is displayed

  Scenario: Book flight (uid:2561dbff-3142-409d-8e1a-71b2d6e8a118)
    # As a Mercury Tours user
    # I want to book a flight
    # and validate my choices
    Given User Signs in with Username "JohnDoeSkunkDemo" and Password "SkunkDemo123"
    When User chooses to fly from "London" to "Paris"
    And User chooses to fly on the "5" of "April"
    And User chooses to return on the "7" of "May"
    And User clicks continue after entering flight details
    Then The select a flight page is displayed
    And Flight page displays destinations as from "London" to "Paris"
    And Flight page displays the departure date as "4/5/2017" and the return as "5/7/2017"

  Scenario: Pay for flight (uid:6a273cf7-b598-4c4d-85c8-bdde3712beae)
    # As a Mercury Tours user who has booked a flight
    # I would like to pay for the flight
    Given The user confirmed their flights
    When User selects their flight
    And User clicks continue after selecting flights
    Then The book a flight page is displayed
    When User fills in passenger and billing details with first name "Mister" middle name "Money" and last name "Bags"
    And User clicks secure purchase
    Then The confirmation page is displayed with "Mister Money Bags" paying the bill
