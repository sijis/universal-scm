import pytest

from universalscm import UniversalSCM
from universalscm.exceptions import SCMError

API = UniversalSCM(provider='tests', api_version='v1')

def test_http_put():
    """Basic PUT request."""
    result = API.put()
    assert 'put' in result['url']

def test_http_put_nested():
    """Basic nested PUT request."""
    result = API.put.anything()
    assert 'PUT' in result['method']

def test_http_put_data():
    """Basic PUT request with data."""
    data = {'data': 'hi'}
    result = API.put.anything(data=data)
    assert data == result['form']

def test_http_put_parameter():
    """Basic PUT request with parameter."""
    result = API.put.param(param='parameter1')
    assert 'parameter1' in result['url']

def test_http_put_parameter_bad():
    """Basic PUT request with bad parameter."""
    with pytest.raises(SCMError):
        result = API.put.param(bad='parameter1')
