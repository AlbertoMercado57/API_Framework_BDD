# Created by albertomercado at 12/20/23
Feature: # Get Product list
  # Enter feature description here

  Scenario:  Scenario: Get the product list
    Given User is in the home page
    When User request a list for the products
    Then User gets the list of product and status code of 200