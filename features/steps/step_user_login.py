from behave import given, when, then
from hamcrest import *
from requests import request
from requests.auth import HTTPBasicAuth


@given(u'the username "{username}"')
def step_impl(context, username):
    context.username = username


@given(u'the password "{password}"')
def step_impl(context, password):
    context.password = password


@when(u'I send a "{method}" request to the "{endpoint}" endpoint')
def step_impl(context, method, endpoint):
    auth = HTTPBasicAuth(context.username, context.password)
    context.response = request(method, context.base_uri + endpoint, auth=auth)


@then(u'I should receive a "{status_code}" status code')
def step_impl(context, status_code):
    assert_that(context.response.status_code, equal_to(int(status_code)))


@then(u'the response should be in JSON format')
def step_impl(context):
    context.json_response = context.response.json()
    assert_that(context.response.json(), is_(dict))


@then(u'the response should contain a JWT')
def step_impl(context):
    context.json_response = context.response.json()
    assert_that(context.json_response, has_key('jwt'))


@then(u'the response should contain an error message')
def step_impl(context):
    assert_that(context.json_response, has_key('message'))
    assert_that(context.json_response['message'], equal_to('Invalid credentials.'))


@given(u'the email "{email}"')
def step_impl(context, email):
    context.email = email


@given(u'the name "{name}"')
def step_impl(context, name):
    context.name = name


@given(u'the age "{age}"')
def step_impl(context, age):
    context.age = age


@when(u'I format this data as json')
def step_impl(context):
    context.user_json = {
        'email': context.email,
        'username': context.username,
        'password': context.password,
        'name': context.name,
        'age': context.age,
    }



