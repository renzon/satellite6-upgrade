"""All the variants those changes during upgrade and the helper functions"""

import os


class VersionError(Exception):
    """Error due to Unsupported Satellite Version"""


_supported_ver = ['6.1', '6.2']
_FROM_VERSION = os.environ.get('FROM_VERSION')
_TO_VER = os.environ.get('TO_VERSION')

if _FROM_VERSION not in _supported_ver:
    raise VersionError(
        'Unsupported preupgrade version {} provided for '
        'entity variants existence tests'.format(_FROM_VERSION))

if _TO_VER not in _supported_ver:
    raise VersionError(
        'Unsupported postupgrade version {} provided for '
        'entity variants existence tests'.format(_TO_VER))

# dict where key is component and value is a dict of properties which name
# changed from satellite 6.1 to 6.2.
# On this last dict the key is the property's name on 6.1 and value the name
#  on 6.2
_SAT_6_DOT_1_TO_6_DOT_2 = {
    'filter': {
        'lookupkey': 'variablelookupkey',
        '(miscellaneous)': 'foremanopenscap::arfreport',
        'organization': 'katello::subscription',
        'configtemplate': 'provisioningtemplate',
        'view_templates, create_templates, edit_templates, '
        'destroy_templates, deploy_templates':
            'view_provisioning_templates, create_provisioning_templates, '
            'edit_provisioning_templates, destroy_provisioning_templates, '
            'deploy_provisioning_templates'
    }
}


def property_name_on_post_version(component, pre):
    """If a component property changes from on versions to another this
    function returns the respective updated name. Otherwise returns the
    unchanged name. This way, to check if a property is present after
    upgrade the test can (suppose upgrade from 6.1 to 6.2) :
    >>> property_name_on_post_version('filter', 'lookupkey')
    'variablelookupkey'

    :param component: str
    :param pre: str
    :return: str
    """
    if component not in _SAT_6_DOT_1_TO_6_DOT_2:
        return pre
    return _SAT_6_DOT_1_TO_6_DOT_2[component].get(pre, pre)
