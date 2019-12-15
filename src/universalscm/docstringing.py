"""Custom docstring updating for dynamic methods."""
import logging
from collections import OrderedDict
from inspect import Parameter, Signature

LOG = logging.getLogger(__name__)


def update_docstring(instance):
    """Update docstring for constructed method.

    Returns:
        str: Discovered docstring from definition.

    """
    try:
        docstring = instance.api_map['doc']
    except (KeyError, TypeError):
        docstring = 'No docstring provided.'

    instance.__class__.__doc__ = docstring
    instance.__class__.__call__.__signature__ = construct_signature(instance)

    return docstring


def construct_signature(instance):
    """Construct a pretty function signature for dynamic commands.

    Returns:
        inspect.Signature: Method signature for command.

    """
    param_dict = OrderedDict()

    valid_params = get_all_valid_params(instance)

    for param, default in sorted(valid_params.items()):
        new_param = Parameter(param, Parameter.KEYWORD_ONLY, default=default)
        LOG.debug('New parameter: %s', new_param)

        param_dict[new_param] = param
        LOG.debug('Parameter dictionary growing: %s', param_dict)

    LOG.debug('Parameter dictionary: %s', param_dict)

    new_signature = Signature(parameters=param_dict)
    LOG.debug('New signature: %s', new_signature)

    return new_signature


def get_all_valid_params(instance):
    """Make a list of valid parameters.

    This accumulates all known parameters from any keys embedded in _path_,
    _default_params_, and _valid_params_.

    Returns:
        Dict of all valid parameters for command in _{key: default}_
        format.

    """
    params = {}

    path_params = instance.find_path_keys(instance.api_map.get('path', ''))
    for param in path_params:
        params[param] = ''

    # Always make a list of valid parameters from endpoint mapping
    valid_params = instance.api_map.get('valid_params', [])
    if isinstance(valid_params, str):
        valid_params = [valid_params]

    for param in valid_params:
        params[param] = ''

    params.update(instance.api_map.get('default_params', {}))

    LOG.debug('Full list of params: %s', params)
    return params
