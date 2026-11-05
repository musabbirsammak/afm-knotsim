import numpy as np
import pytest

from knotsim.chains.templates import TEMPLATES, get_template

IMPLEMENTED = ["0_1", "3_1", "4_1"]


@pytest.mark.parametrize("name", IMPLEMENTED)
def test_template_shape(name):
    c = get_template(name, n_points=150)
    assert c.shape == (150, 3)
    assert np.isfinite(c).all()


@pytest.mark.parametrize("name", IMPLEMENTED)
def test_template_closed_and_evenly_sampled(name):
    """Closing bond (last -> first) should be about as long as the other bonds."""
    c = get_template(name, n_points=400)
    bonds = np.linalg.norm(np.diff(c, axis=0, append=c[:1]), axis=1)
    assert bonds[-1] < 3.0 * np.median(bonds)


@pytest.mark.parametrize("name", IMPLEMENTED)
def test_template_not_self_intersecting(name):
    """Non-adjacent beads stay apart, so the seed is a valid embedded curve."""
    c = get_template(name, n_points=200)
    d = np.linalg.norm(c[:, None, :] - c[None, :, :], axis=-1)
    n = len(c)
    idx = np.arange(n)
    sep = np.abs(idx[:, None] - idx[None, :])
    sep = np.minimum(sep, n - sep)
    bond = np.median(np.linalg.norm(np.diff(c, axis=0), axis=1))
    assert d[sep > 3].min() > 0.5 * bond


def test_unknown_topology_raises():
    with pytest.raises(KeyError):
        get_template("9_42")


def test_registry_lists_all_targets():
    assert {"0_1", "3_1", "4_1", "5_1", "5_2", "6_1", "2^2_1"} <= set(TEMPLATES)
