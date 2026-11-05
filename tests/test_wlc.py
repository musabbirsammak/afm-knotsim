import pytest

pytestmark = pytest.mark.skip(reason="wlc_mc.relax not implemented yet")


def test_relax_preserves_topology():
    """After relaxation, identify_knot(relaxed) == identify_knot(template)."""


def test_persistence_length_recovered():
    """Tangent correlation decay of relaxed chains matches the configured Lp within tolerance."""
