"""Seed 3D coordinates for each target topology.

A template is a closed polygon with the right knot type. It is only a starting shape: the
worm-like-chain Monte Carlo in ``wlc_mc.py`` relaxes it into a realistic conformation while
preserving topology.

Knots return one chain of shape (N, 3). Links (catenanes) return a list of chains.
Points are not repeated: chain[-1] connects back to chain[0].
"""

from __future__ import annotations

from typing import Callable

import numpy as np

Chain = np.ndarray  # shape (N, 3)


def _t(n_points: int) -> np.ndarray:
    return np.linspace(0.0, 2.0 * np.pi, n_points, endpoint=False)


def unknot(n_points: int = 200) -> Chain:
    """Planar circle of unit radius (knot 0_1)."""
    t = _t(n_points)
    return np.stack([np.cos(t), np.sin(t), np.zeros_like(t)], axis=1)


def trefoil(n_points: int = 200) -> Chain:
    """Trefoil knot (3_1), standard parametrisation."""
    t = _t(n_points)
    x = np.sin(t) + 2.0 * np.sin(2.0 * t)
    y = np.cos(t) - 2.0 * np.cos(2.0 * t)
    z = -np.sin(3.0 * t)
    return np.stack([x, y, z], axis=1)


def figure_eight(n_points: int = 200) -> Chain:
    """Figure-eight knot (4_1), Lissajous-style parametrisation."""
    t = _t(n_points)
    r = 2.0 + np.cos(2.0 * t)
    x = r * np.cos(3.0 * t)
    y = r * np.sin(3.0 * t)
    z = np.sin(4.0 * t)
    return np.stack([x, y, z], axis=1)


def torus_knot_5_1(n_points: int = 300) -> Chain:
    """(5,2) torus knot, i.e. 5_1. TODO: implement and verify with topology.identify."""
    raise NotImplementedError


def twist_knot_5_2(n_points: int = 300) -> Chain:
    """Twist knot 5_2. TODO: build from a twist-knot construction and verify."""
    raise NotImplementedError


def twist_knot_6_1(n_points: int = 300) -> Chain:
    """Twist knot 6_1. TODO."""
    raise NotImplementedError


def hopf_link(n_points: int = 200) -> list[Chain]:
    """Two-ring catenane (Hopf link, 2^2_1). TODO: two interlocked circles."""
    raise NotImplementedError


TEMPLATES: dict[str, Callable[..., Chain | list[Chain]]] = {
    "0_1": unknot,
    "3_1": trefoil,
    "4_1": figure_eight,
    "5_1": torus_knot_5_1,
    "5_2": twist_knot_5_2,
    "6_1": twist_knot_6_1,
    "2^2_1": hopf_link,
}


def get_template(name: str, n_points: int = 200) -> Chain | list[Chain]:
    """Return seed coordinates for topology ``name`` (e.g. "3_1")."""
    if name not in TEMPLATES:
        raise KeyError(f"Unknown topology {name!r}. Available: {sorted(TEMPLATES)}")
    return TEMPLATES[name](n_points)
