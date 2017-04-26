"""Upgrade TestSuite for validating Satellite architectures existence
post upgrade

:Requirement: Upgraded Satellite

:CaseAutomation: Automated

:CaseLevel: Acceptance

:CaseComponent: CLI

:TestType: NonFunctional

:CaseImportance: High

:Upstream: No
"""
import pytest
from upgrade_tests.helpers.existence import compare_postupgrade


@pytest.mark.parametrize(
    "pre,post",
    compare_postupgrade('architecture', 'name')
)
def test_positive_architectures_by_name(pre, post):
    """Test all architectures are existing after upgrade by names

    :id: eb6d3728-6b0b-4cb7-888e-8d64a46e7beb

    :expectedresults: All architectures should be retained post upgrade by
        names
    """
    assert pre == post
