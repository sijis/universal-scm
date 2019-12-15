"""GitHub v3 API description."""
DEFAULT_URL = 'https://api.github.com'
API_PATH = ''

MAPPING = {
    'root': {
        'doc': 'Show API URLs.',
        'path': '/',
    },
    'user': {
        'path': '/user',
    },
    'users': {
        'path': '/users',
        '{id}': {
            'path': '/users/{id}',
        },
    },
    'repos': {
        'owner': {
            'path': 'repos/${owner}',
            'repo': {
                'path': 'repos/${owner}/${repo}',
            }
        }
    }
}


def auth(self):
    """Set authentication."""
    self.headers.update({
        'Authorization': 'token {0}'.format(self.token),
    })
    return self.headers
