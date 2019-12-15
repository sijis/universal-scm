
import pytest

from universalscm import UniversalSCM
from universalscm.exceptions import SCMError

API = UniversalSCM(provider='tests', api_version='v1')

def test_http_get():
    """Basic GET request."""
    result = API.get()
    assert 'get' in result['url']

def test_http_get_querystring():
    """Basic GET querystring request."""
    qs = {'hello': 'world'}
    result = API.get(data=qs)
    assert qs == result['args']

def test_http_get_nested():
    """Basic nested GET request."""
    result = API.get.anything()
    assert 'GET' in result['method']

def test_http_get_parameter():
    """Basic GET request with parameter."""
    result = API.get.param(param='parameter1')
    assert 'parameter1' in result['url']

def test_http_get_parameter_bad():
    """Basic GET request with bad parameter."""
    with pytest.raises(SCMError):
        result = API.get.param(bad='parameter1')
