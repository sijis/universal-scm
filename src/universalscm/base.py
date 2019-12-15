"""Python interface to SCM REST APIs."""
import importlib
import logging
import types
from pprint import pformat
from string import Template

import murl

from . import common_methods
from .scm_command import SCMCommand


class UniversalSCM:
    """Python API Wrapper for SCM."""

    __dir__ = common_methods.dynamic_dir

    def __init__(self, provider=None, api_version=None, token='', username='', password='', url='', port=None,
                 **kwargs):
        """SCM object for interacting with the API.

        Optional parameters for HTTP Basic Authentication or API token. Token is
        preferred by most providers.

        Parameters:
            kwargs (dict): Various configuration options.
            password (str): Basic authentication password.
            port (int): HTTP port to use.
            provider (str): A provider such as gitlab, github, localhost.
            token (str): API token.
            url (str): Base URL of provider, e.g. https://gitlab.com.
            username (str): Basic authentication user.
            api_version (int): API version of provider to use.

        """
        self.log = logging.getLogger(__name__)
        self.log.debug('Received parameters:\n%s', pformat(locals()))

        _ = kwargs
        self.data = {}
        self.headers = {
            'User-agent': 'SCM Python Library v0.0.1',
        }

        self.provider = provider
        self.api_version = api_version

        self.token = token
        self.username = username
        self.password = password

        self.module = self.loader()
        self.auth = types.MethodType(self.module.auth, self)
        self.api_map = self.module.MAPPING

        _url = murl.Url(url or self.module.DEFAULT_URL)

        if port:
            _url.port = port

        _url.path = self.module.API_PATH

        self.url = _url

    def __getattr__(self, api_call):
        """Execute dynamic method and pass keyword args as data to API call."""
        return SCMCommand(self, api_call, self.api_map)

    def loader(self):
        """Load Provider API version Module."""
        path = '.providers.{}_{}'.format(self.provider, self.api_version)
        lib = importlib.import_module(path, package=__package__)
        self.log.info('Loading library: %s', lib)
        return lib

    # def get_auth(self):
    #     """Get username and password for request authentication.
    #
    #     Returns:
    #         dict: Empty if no authentication specified, otherwise return::
    #
    #             {'auth': (username, password)}
    #
    #     """
    #     auth = {}
    #     if self.username and self.password:
    #         auth['auth'] = (self.username, self.password)
    #     return auth

    def format_url(self, path, kwargs):
        """Format request URL with endpoint mapping.

        Substitute `${}` placeholders with data from keywords. This removes the
        key from the dict to prevent reuse in parameters.

        Args:
            path: URL path string to use, e.g. /application
            kwargs: Dict containing any keys that need to be substituted in
                _path_.

        Returns:
            str: Fully constructed URL string with substitutions in place.

        """
        self.log.debug('URL formatter:\n%s', pformat(locals()))

        # Substitute mustache '${}' placeholders with data from keywords
        substitute_path = Template(path).substitute(kwargs)
        self.log.debug('URL substitute_path: %s', substitute_path)

        url = '{0}{1}'.format(self.url, substitute_path)
        self.log.debug('Full formatted URL: %s', url)

        return url
