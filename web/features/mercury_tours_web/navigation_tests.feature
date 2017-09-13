@nav
Feature: Navigation tests
    As a web user or Mercury Tours
    I want to navigate around the website
    When signed in or not

  Background:
    Given The landing page is open

  Scenario: Navigation when user is not signed in (uid:acd5fdcc-0aa8-4cb6-a603-bac384cb7130)
    # As a web user 
    # I would like to navigate around Mercury Tours
    # Without signing in
    When User clicks the register tab
    Then The register page is displayed
    When User clicks the cruises tab
    Then The cruises page is displayed
    When User clicks the flight tab
    Then The landing page is displayed
    When User clicks the sign-on tab
    Then The sign-on page is displayed

  Scenario: Navigation when user is signed in (uid:904ae545-091c-46b3-8f40-7a1df29bad00)
    # As a Mercury Tours user 
    # I would like to navigate around Mercury Tours
    # and Validate I am signed in
    Given User Signs in with Username "JohnDoeSkunkDemo" and Password "SkunkDemo123"
    When User clicks itinerary tab
    Then The itinerary page is displayed
    When User clicks sign-off tab
    Then The sign-on page is displayed
