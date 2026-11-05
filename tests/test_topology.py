import pytest

from knotsim.chains.templates import get_template
from knotsim.chains.topology import identify_knot

pytestmark = pytest.mark.skip(reason="topology.identify_knot not implemented yet")


@pytest.mark.parametrize("name", ["0_1", "3_1", "4_1"])
def test_templates_have_expected_knot_type(name):
    assert identify_knot(get_template(name)) == name
