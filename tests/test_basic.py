"""Basic tests."""
from universalscm import UniversalSCM

API = UniversalSCM(provider='tests', api_version='v1')

def test_basic_setup():
    """Basic instantiation."""
    assert API.provider == 'tests'
    assert API.api_version == 'v1'
    assert type(API.api_map) == dict

def test_basic_useragent():
    """User Agent test."""
    result = API.useragent()
    assert 'SCM Python Library' in result['user-agent']
