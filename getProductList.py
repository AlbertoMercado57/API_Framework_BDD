from pytest_bdd import scenario, given, when, then
import requests

@given("User is in the home page")
def step_impl(context):
    context.products = requests.get('https://automationexercise.com')


@when("User request a list for the products")
def step_impl(context):
    context.products = requests.get('https://automationexercise.com/api/productsList')


@then("User gets the list of product and status code of 200")
def step_impl(context):
    status_code = context.products.status_code
    assert status_code == 200
    response = context.products.json()
    print(response)

