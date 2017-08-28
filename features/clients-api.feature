Feature: User registration
  In order to add a new client to the clients api
  As an api user
  I want to post the client data to the /clients api endpoint

  Scenario: Register a new client
     Given I setup a new client
      When I post the client data to the endpoint
      Then I receive the http code 201 in the response