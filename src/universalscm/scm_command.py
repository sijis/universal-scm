"""SCM API walker and caller."""
import json
import logging
from pprint import pformat
from string import Template

import requests

from . import common_methods
from .docstringing import update_docstring
from .exceptions import SCMError


class SCMCommand(object):
    """Dynamic construction of attributes based on endpoint mapping table.

    Instead of writing out each API endpoint as a method here or binding
    the API endpoints at instance runttime, we can simply use an elegant
    Python technique to construct method execution on- demand. We simply
    provide a mapping table between SCM API calls and function names
    (with necessary parameters to replace embedded keywords on GET or json
    data on POST/PUT requests).

    __getattr__() is used as callback method implemented so that when an
    object tries to call a method which is not defined here, it looks to
    find a relationship in the the mapping table.  The table provides the
    structure of the API call and parameters passed in the method will
    populate missing data.

    Raises:
        AttributeError: Attribute is not part of the mapping table.

    Returns:
        dict: JSON returned from SCM API.

    TODO:
        Should probably url-encode GET query parameters on replacement

    """

    __dir__ = common_methods.dynamic_dir

    def __init__(self, client, api_call, menu, parent='SCM'):
        super(SCMCommand, self).__init__()
        self.log = logging.getLogger(__name__)

        self.log.debug('Received parameters:\n%s', pformat(locals()))
        self.__name__ = '.'.join([parent, api_call])
        self.log.debug('Command name: %s', self.__name__)

        self.client = client
        self.api_call = api_call

        # Missing method is also not defined in our mapping table
        try:
            self.api_map = menu[self.api_call]
            self.log.debug('API map:\n%s', pformat(self.api_map))
        except KeyError:
            raise AttributeError(('Method "{0}" does not exist.\n'
                                  'Options available are: {1}').format(self.api_call, menu.keys()))

        update_docstring(self)

    def __getattr__(self, command):
        """Recursively generate objects for endpoints.

        Returns:
            SCMCommand: Next callable API.

        """
        next_api = self.api_map.get(command, None)

        if isinstance(next_api, dict):
            self.log.debug('Next API level: %s', next_api)
            next_api = SCMCommand(
                self.client,
                command,
                self.api_map,
                parent=self.__name__,
            )
        else:
            self.log.debug('Reached leaf "%s" of map: %s', command, next_api)

        return next_api

    def __call__(self, **kwargs):
        """Construct request call to SCM API.

        Args:
            **kwargs: Only excepts keywords used in the endpoint mapping
                _path_, _valid_params_, and _default_params_.

        Returns:
            dict: JSON from SCM.

        Raises:
            TypeError: If an unexpected keyword was passed in.

        """
        self.log.debug('__call__ locals():\n%s', pformat(locals()))

        method = self.determine_method(kwargs)
        self.validate_params(kwargs)
        url = self.client.format_url(self.api_map['path'], kwargs)

        body = self.construct_body(kwargs)

        if method == 'GET':
            action = 'params'
        else:
            action = 'data'

        self.client.auth()

        url_params = {
            'url': url,
            action: body,
            'headers': self.client.headers,
            'timeout': 15,
        }

        # auth = self.client.get_auth()
        # url_params.update(auth)

        response = self._request(method, url_params)

        return response.json()

    def _request(self, method, url_params):
        """Make HTTP request (data replacements are finalized)."""
        self.log.debug('Request type: %s; Payload:\n%s\n[auth] redacted', method.lower(),
                       pformat(dict((key, value) for key, value in url_params.items() if key != 'auth')))
        response = getattr(requests, method.lower())(**url_params)

        self.log.debug('Response code: [%d]; Response text: %s', response.status_code, response.text)
        response.raise_for_status()

        return response

    def construct_body(self, kwargs):
        """Form body of request passed from ``data`` or in ``args``.

        Returns:
            dict: Body of request, e.g.::

                requests.get(url, params=body)
                requests.post(url, data=body)

        """
        # Provide a JSON object override
        if 'json' in kwargs:
            return json.dumps(kwargs['json'])

        body = {}
        body.update(self.api_map.get('default_params', {}))
        body.update(kwargs.pop('data', None) or self.client.data)
        body.update(kwargs)
        self.log.debug('Request body to send: %s', body)

        return body

    def determine_method(self, kwargs):
        """Determine which HTTP method we should use."""
        valid_methods = self.api_map.get('method', ['GET'])
        passed_method = kwargs.get('method', '').upper()

        # Use the method passed
        if passed_method:
            if passed_method in valid_methods:
                return passed_method
            else:
                error = 'Valid methods are {}, we received "{}".'.format(valid_methods, passed_method)
                raise SCMError(error)

        # Let's fallback to something gracefully.
        if isinstance(valid_methods, list):
            methods_order = ['GET', 'POST', 'PUT', 'DELETE']
            for method in methods_order:
                if method in valid_methods:
                    return method

    def validate_params(self, kwargs):
        """Validate remaining kwargs against valid_params."""
        self.log.debug('Validate Params (kwargs): %s', kwargs)
        valid_params = self.api_map.get('valid_params', [])
        path_keys = self.find_path_keys(self.api_map['path'])
        method_keys = ['method']
        default_parameter_keys = ['data']
        all_valid_params = valid_params + path_keys + method_keys + default_parameter_keys
        self.log.debug('Valid parameters: %s', all_valid_params)

        for keyword in kwargs:
            if keyword not in all_valid_params:
                if 'default_params' not in self.api_map:
                    raise SCMError('Was not expecting any arguments.')
                elif keyword not in self.api_map['default_params']:
                    raise SCMError(('{0}() got an unexpected keyword ' 'argument "{1}"').format(self.api_call, keyword))

        for key in path_keys:
            if key not in kwargs:
                raise SCMError('Missing "{}" in keyword argument.'.format(key))

    def find_path_keys(self, path):
        """Extract keys from the path.

        Args:
            path: String of endpoint path with possible _${parameter}_
            templated parameters.

        Returns:
            List of parameters found in endpoint path.

        """
        template_keys = Template.pattern.findall(path)
        path_keys = [param[2] for param in template_keys]

        self.log.debug('Path keys: %s; Found in template: %s', path_keys, template_keys)

        return path_keys
