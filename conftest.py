import inspect
import pytest


from parse import parse
from webob import Request, Response
from requests import Session as RequestsSession
from wsgiadapter import WSGIAdapter as RequestsWSGIAdapter
from api import API


@pytest.fixture
def client(api):
    return api.test_session()