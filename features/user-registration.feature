Feature: User registration
  In order to register a new user
  As an api user
  I want to send a post request with the user json format to the /user endpoint
  Users should be authenticated to create a new user

  Scenario: Register a user
    Given the username "username"
    And the password "password"
    And the email "username@domain.com"
    And the name "User Name"
    And the age "28"
    When I format this data as json
    And I send a "post" request to the "/users" endpoint with the user data
    Then I should receive a "201" status code
    And the response should be in JSON format
    And the response should contain the ser id

  Scenario: Register a user with username already registered
    Given a random user with username "username"
    And another user with the same username
    When I post both users to the /users endpoint
    Then I should receive a 409 status code
    And the response should be in json

    And the response should the message informing the resource already exists

  Scenario: Register a user with email already registered
    Given the a random user with email "user@domain.com"
    And another user with the same email
    When I post both users to the /users endpoint
    Then I should receive a 409 status code
    And the response should be in json
    And the response should the message informing the resource already exists

  Scenario: Register a user missing username
    Given a random user missing its username
    When I post the users to the /users endpoint
    Then I should receive a 400 status code
    And the response should be in json
    And the response should the message informing the resource already exists

  Scenario: Register a user missing password

  Scenario: Register a user missing name

  Scenario: Register a user missing email

  Scenario: Register a user missing age