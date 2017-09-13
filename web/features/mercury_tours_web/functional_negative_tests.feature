@neg
Feature: Functional Negative tests
    As a user
    I want to try and use the functionality of Mercury Tours

  Background:
    Given The landing page is open

  Scenario Outline:  Sign in with invalid details (uid:8313c756-e36f-407a-9bd8-db3fe34ad777)
    # As a web user
    # I want to try sign in with bad credentials
    When User clicks the sign-on tab
    Then The sign-on page is displayed
    When User fills in signs on form with Username "<userName>" and Password "<password>"
    And User clicks the login submit form
    Then The sign-on page is displayed

    Examples:
      | userName | password | hiptest-uid |
      | TestNameNotaUser | skunkwrongpass123 | uid:62ba1633-f3c1-4175-b98f-0a665fab64ee |
      | JohnDoeSkunk | skunkwrongpass123 | uid:1008c820-e73a-4148-8623-3b8429c7ca3b |
      | InvalidUser889 | skunkwrongpass123 | uid:6d38006d-5ede-4f1f-a610-ccd3ad0c49f5 |
      | JohnDoeSkunkDemo | SkunkDemo123 | uid:93be39b5-a693-4b9e-83ef-022b00460642 |

  Scenario: Validate menu values when signed in (uid:9c991d8c-6405-48dc-9e1f-d5668620d64b)
    # As a Mercury Tours user
    # I would like the validate that the correct menus are displayed
    # When I am  signed in
    Then The menu is displayed as "SIGN-ON REGISTER SUPPORT CONTACT"
    Given User Signs in with Username "JohnDoeSkunkDemo" and Password "SkunkDemo123"
    Then The menu is displayed as "SIGN-OFF ITINERARY PROFILE SUPPORT CONTACT"
    When User clicks the cruises tab
    Then The menu is displayed as "SIGN-OFF ITINERARY PROFILE SUPPORT CONTACT"
