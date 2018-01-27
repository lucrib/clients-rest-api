#language: en

Feature: User login
  In order to login to the api
  As an api user
  I want to send a get request to the /login endpoint and receive a JSON Web Token as response
  The response should be in json format
  If I send a wrong combination of user/password I should receive a 403 http status code

  Scenario: Login to the api with valid credentials
    Given the username "username"
    And the password "password"
    When I send a "get" request to the "/login" endpoint
    Then I should receive a "200" status code
    And the response should be in JSON format
    And the response should contain a JWT

  Scenario: Login to the api with invalid credentials
    Given the username "wronguser"
    And the password "wrongpass"
    When I send a "get" request to the "/login" endpoint
    Then I should receive a "401" status code
    And the response should be in JSON format
    And the response should contain an error message
