"""Upgrade TestSuite for validating Satellite role filters existence and
associations post upgrade

:Requirement: Upgraded Satellite

:CaseAutomation: Automated

:CaseLevel: System

:CaseComponent: CLI

:TestType: nonfunctional

:CaseImportance: High

:SubType1: installability

:Upstream: No
"""
from functools import partial

import pytest

from upgrade_tests.helpers.existence import compare_postupgrade, pytest_ids

# Required Data
compare_filter = partial(compare_postupgrade, 'filter')
fil_rtype = compare_filter('resource type')
fil_search = compare_filter('search')
fil_unlimited = compare_filter('unlimited?')
fil_role = compare_filter('role')
fil_perm = compare_filter('permissions')


@pytest.mark.parametrize(
    "pre,post,msg", fil_rtype, ids=pytest_ids(fil_rtype))
def test_positive_filters_by_resource_type(pre, post, msg):
    """Test all filters of all roles are existing after upgrade by resource
    types

    :id: upgrade-362f4b0c-49bb-424d-92e4-446ec59b8c5c

    :expectedresults: All filters of all roles should be retained post upgrade
        by resource types
    """
    if msg != '':
        pytest.fail(msg)
    assert pre == post


@pytest.mark.parametrize(
    "pre,post,msg", fil_search, ids=pytest_ids(fil_search))
def test_positive_filters_by_search(pre, post, msg):
    """Test all filters search criteria is existing after upgrade

    :id: upgrade-da2dd076-f0e6-45ee-8a5d-99f2e083aabc

    :expectedresults: All filters search criteria should be retained post
        upgrade
    """
    if msg != '':
        pytest.fail(msg)
    assert pre == post


@pytest.mark.parametrize(
    "pre,post,msg", fil_unlimited, ids=pytest_ids(fil_unlimited))
def test_positive_filters_by_unlimited_check(pre, post, msg):
    """Test all filters unlimited criteria is existing after upgrade

    :id: upgrade-abf65640-dc9b-415e-846d-0df43391228f

    :expectedresults: All filters unlimited criteria should be retained post
        upgrade
    """
    if msg != '':
        pytest.fail(msg)
    assert pre == post


@pytest.mark.parametrize("pre,post,msg", fil_role, ids=pytest_ids(fil_role))
def test_positive_filters_by_role(pre, post, msg):
    """Test all filters association with role is existing after upgrade

    :id: upgrade-dffdc0ac-a4b5-4b70-8e4d-fb37765f75ed

    :expectedresults: All filters association with role should be retained post
        upgrade
    """
    if msg != '':
        pytest.fail(msg)
    assert pre == post


@pytest.mark.parametrize("pre,post,msg", fil_perm, ids=pytest_ids(fil_perm))
def test_positive_filters_by_permissions(pre, post, msg):
    """Test all filters all permissions are existing after upgrade

    :id: upgrade-dd4fab7e-bd8f-4645-8aab-42a14ffe3a0e

    :expectedresults: All filters all permissions should be retained post
        upgrade
    """
    if msg != '':
        pytest.fail(msg)
    assert pre == post
