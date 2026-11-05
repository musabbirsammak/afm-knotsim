"""Worm-like-chain Monte Carlo relaxation of closed DNA chains.

Energy: discrete bending energy with persistence length Lp,
    E_bend / kT = (Lp / b) * sum_i (1 - cos theta_i),
where b is the bead spacing and theta_i the angle between consecutive bonds.
Self-avoidance: beads closer than the excluded-volume diameter are rejected, which also stops the
chain passing through itself. Topology is rechecked every ``topology_check_every`` steps.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np


@dataclass
class WLCParams:
    bead_size_nm: float = 2.5
    persistence_length_nm: float = 50.0
    excluded_volume_nm: float = 2.5
    mc_steps: int = 20000
    topology_check_every: int = 500
    p_crankshaft: float = 0.7


def resample_to_bead_size(chain: np.ndarray, contour_length_nm: float, bead_size_nm: float) -> np.ndarray:
    """Rescale a template to the target contour length and resample at even bead spacing.

    TODO.
    """
    raise NotImplementedError


def bending_energy(chain: np.ndarray, params: WLCParams) -> float:
    """Bending energy in units of kT for a closed chain. TODO."""
    raise NotImplementedError


def crankshaft_move(chain: np.ndarray, rng: np.random.Generator) -> np.ndarray:
    """Rotate the segment between two random beads about the axis joining them. TODO."""
    raise NotImplementedError


def relax(chain: np.ndarray, params: WLCParams, rng: np.random.Generator) -> np.ndarray:
    """Metropolis MC relaxation that preserves topology. Returns the final conformation. TODO."""
    raise NotImplementedError
