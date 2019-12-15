import pytest

from universalscm import UniversalSCM
from universalscm.exceptions import SCMError

API = UniversalSCM(provider='tests', api_version='v1')

def test_http_post():
    """Basic POST request."""
    result = API.post()
    assert 'post' in result['url']

def test_http_post_nested():
    """Basic nested POST request."""
    result = API.post.anything()
    assert 'POST' in result['method']

def test_http_post_data():
    """Basic POST request with data."""
    data = {'data': 'hi'}
    result = API.post.anything(data=data)
    assert data == result['form']

def test_http_post_parameter():
    """Basic POST request with parameter."""
    result = API.post.param(param='parameter1')
    assert 'parameter1' in result['url']

def test_http_post_parameter_bad():
    """Basic POST request with bad parameter."""
    with pytest.raises(SCMError):
        result = API.post.param(bad='parameter1')
