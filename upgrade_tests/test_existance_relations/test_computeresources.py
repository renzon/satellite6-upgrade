"""Upgrade TestSuite for validating Satellite compute resources existence and
associations post upgrade

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
    compare_postupgrade('compute-resource', 'name')
)
def test_positive_compute_resources_by_name(pre, post):
    """Test all compute resources are existing post upgrade by their name

    :id: 24f05707-4547-458c-bb7e-96be35d3f043

    :expectedresults: All compute resources should be retained post upgrade
    """
    assert pre == post


@pytest.mark.parametrize(
    "pre,post",
    compare_postupgrade('compute-resource', 'provider')
)
def test_positive_compute_resources_by_provider(pre, post):
    """Test all compute resources provider are existing post upgrade

    :id: f3429be3-505e-44ff-a4fb-4adc940e8b67

    :expectedresults: All compute resources provider should be retained post
        upgrade
    """
    assert pre == post
