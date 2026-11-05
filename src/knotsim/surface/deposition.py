"""Deposit a relaxed 3D chain onto mica.

Two modes, matching the two regimes discussed in the AFM DNA literature:
- kinetic_trapping: random rotation, then project to the xy plane while keeping z for z-order.
- equilibration_2d: further MC in 2D with strand passage forbidden at crossings.

Output keeps the z coordinate so over/under can be read off at every crossing.
"""

from __future__ import annotations

import numpy as np


def random_rotation(chain: np.ndarray, rng: np.random.Generator) -> np.ndarray:
    """Apply a uniformly random 3D rotation. TODO (scipy.spatial.transform.Rotation.random)."""
    raise NotImplementedError


def deposit(chain: np.ndarray, mode: str, rng: np.random.Generator) -> np.ndarray:
    """Return the deposited chain, shape (N, 3): xy on the surface, z kept for z-order. TODO."""
    raise NotImplementedError
