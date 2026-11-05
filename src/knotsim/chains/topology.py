"""Topology invariants used as exact labels.

Wraps an established library (topoly by default) rather than reimplementing knot
identification, so labels are trustworthy and reviewers can check them.
"""

from __future__ import annotations

import numpy as np


def identify_knot(chain: np.ndarray) -> str:
    """Return the knot type of a closed chain (shape (N, 3)) in Rolfsen notation, e.g. "3_1".

    TODO: call topoly.alexander(...) on the closed polygon and map the result to a knot name.
    """
    raise NotImplementedError


def linking_number(chain_a: np.ndarray, chain_b: np.ndarray) -> int:
    """Gauss linking number of two closed chains. Hopf link -> |Lk| = 1.

    TODO: discrete Gauss integral, or topoly's linking-number routine.
    """
    raise NotImplementedError


def same_topology(before: np.ndarray, after: np.ndarray) -> bool:
    """True if a Monte Carlo move preserved the knot type. Used to reject strand passages."""
    return identify_knot(before) == identify_knot(after)
