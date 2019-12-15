"""Tests API using httpbin.org."""
DEFAULT_URL = 'http://httpbin.org'
API_PATH = ''

MAPPING = {
    'root': {
        'path': '/',
    },
    'get': {
        'path': '/get',
        'anything': {
            'path': '/anything',
        },
        'param': {
            'path': '/anything/${param}',
        },
    },
    'post': {
        'path': '/post',
        'method': ['POST'],
        'anything': {
            'path': '/anything',
            'method': ['POST'],
        },
        'param': {
            'path': '/anything/${param}',
            'method': ['POST'],
        },
    },
    'put': {
        'path': '/put',
        'method': ['PUT'],
        'anything': {
            'path': '/anything',
            'method': ['PUT'],
        },
        'param': {
            'path': '/anything/${param}',
            'method': ['PUT'],
        },
    },
    'useragent': {
        'path': '/user-agent',
    },
}


def auth(self):
    """Set authentication."""
    return self.headers
