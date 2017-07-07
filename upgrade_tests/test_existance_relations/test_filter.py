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
import pytest

from upgrade_tests.helpers.existence import compare_postupgrade, pytest_ids, \
    check_missing_entity

# Required Data
filter_attrs = []
for attr in ['resource type', 'search', 'unlimited?', 'role', 'permissions']:
    filter_attrs.extend(compare_postupgrade('filter', attr))


@pytest.mark.parametrize(
    "pre,post", filter_attrs, ids=pytest_ids(filter_attrs))
def test_positive_all_filter_attributes(pre, post):
    """Test all filters of all possible filter attributes are present after
    upgrade

    :id: upgrade-362f4b0c-49bb-424d-92e4-446ec59b8c5c

    :expectedresults: All filters of all attributes should be retained post
    upgrade
    """
    msg = check_missing_entity(pre, post)
    if msg:
        pytest.fail(msg)
    assert pre == post
