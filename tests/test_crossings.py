import pytest

pytestmark = pytest.mark.skip(reason="crossings.find_crossings not implemented yet")


def test_planar_circle_has_no_crossings():
    """Unknot lying flat: zero crossings."""


def test_trefoil_projection_has_at_least_three_crossings():
    """Any projection of 3_1 has >= 3 crossings, alternating over/under along the chain."""
