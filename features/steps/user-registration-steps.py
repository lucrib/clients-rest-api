from behave import given, when, then
from hamcrest import *
from requests import request
from requests.auth import HTTPBasicAuth


@when(u'I send a "{method}" request to the "{endpoint}" endpoint with the user data')
def step_impl(context, method, endpoint):
    # auth = HTTPBasicAuth(context.username, context.password)
    context.response = request(method, context.base_uri + endpoint, json=context.user_json)


@then(u'the response should contain the ser id')
def step_impl(context):
    assert_that(context.response.json(), has_key('id'))


@given(u'a random user with username "username"')
def step_impl(context):
    context.user_json = dict(username='username', password='password', email='email', name='name', age=0)


@given(u'another user with the same username')
def step_impl(context):
    context.another_user_json = dict(username='username', password='password', email='email', name='name', age=0)


@when(u'I post both users to the /users endpoint')
def step_impl(context):
    resp = request('post', context.base_uri + '/users', json=context.user_json)
    assert_that(resp.status_code, equal_to(201))
    context.response = request('post', context.base_uri + '/users', json=context.another_user_json)


@then(u'I should receive a 409 status code')
def step_impl(context):
    assert_that(context.response.status_code, equal_to(409))


@then(u'the response should be in json')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the response should be in json')


@then(u'the response should the message informing the resource already exists')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the response should the message informing the resource already exists')


@given(u'the a random user with email "user@domain.com"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the a random user with email "user@domain.com"')


@given(u'another user with the same email')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given another user with the same email')


@given(u'a random user missing its username')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given a random user missing its username')


@when(u'I post the users to the /users endpoint')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I post the users to the /user endpoint')


@then(u'I should receive a 400 status code')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I should receive a 400 status code')
