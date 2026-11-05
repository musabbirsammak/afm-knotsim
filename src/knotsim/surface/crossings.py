"""Find crossings in the 2D projection and label each one over/under.

A crossing is a pair of non-adjacent segments whose xy projections intersect. At each crossing,
the strand with the larger interpolated z is "over". The ordered sequence of crossings along the
chain gives the Gauss code, which the model's topology head can be trained against.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np


@dataclass
class Crossing:
    xy: np.ndarray          # (2,) position in nm
    over_segment: int       # index of the segment on top
    under_segment: int      # index of the segment underneath
    over_param: float       # position along over segment, in [0, 1)
    under_param: float      # position along under segment, in [0, 1)


def find_crossings(chain: np.ndarray) -> list[Crossing]:
    """All crossings of a closed chain's xy projection. TODO (segment intersection, numba)."""
    raise NotImplementedError


def gauss_code(chain: np.ndarray, crossings: list[Crossing]) -> list[int]:
    """Signed Gauss code: +k when passing over crossing k, -k when passing under. TODO."""
    raise NotImplementedError
