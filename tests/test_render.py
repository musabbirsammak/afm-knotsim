import numpy as np

from knotsim.render.artifacts import plane_tilt, scanline_offset


def test_scanline_offset_is_constant_per_row():
    rng = np.random.default_rng(0)
    out = scanline_offset(np.zeros((32, 32)), rng, sigma_nm=0.2)
    assert np.allclose(out.std(axis=1), 0.0)
    assert out[:, 0].std() > 0


def test_plane_tilt_is_linear():
    rng = np.random.default_rng(0)
    out = plane_tilt(np.zeros((16, 16)), rng, max_slope=0.01)
    assert np.allclose(np.diff(out, n=2, axis=0), 0.0)
    assert np.allclose(np.diff(out, n=2, axis=1), 0.0)


# TODO once render/tip.py exists:
# def test_tip_dilation_widens_strand(): measured width > true width, height preserved
