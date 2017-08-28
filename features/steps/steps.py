# coding=utf-8
import httplib as http
import json

from behave import *
from hamcrest import *

from client.model import Client


@given(u'I setup a new client')
def step_impl(context):
    context.client_data = Client('João da Silva', '16/01/1990', 'joao@silva.com')


@when(u'I post the client data to the endpoint')
def step_impl(context):
    data = json.dumps(context.client_data.json())
    content_type = 'application/json'
    context.response = context.client.post('/clients', data=data, content_type=content_type)


@then(u'I receive the http code 201 in the response')
def step_impl(context):
    assert_that(context.response.status_code, is_(equal_to(http.CREATED)), context.response.data)
