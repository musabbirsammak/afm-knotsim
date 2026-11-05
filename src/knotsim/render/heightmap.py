"""Rasterise a deposited chain into an ideal (tip-free) height map.

Each segment is drawn as a tube of height ``dna_height_nm``. At crossings the over-strand sits on
top of the under-strand, so its height is ``crossing_height_factor * dna_height_nm``.
Also returns the label rasters (DNA mask, skeleton) on the same grid.
"""

from __future__ import annotations

import numpy as np


def render_heightmap(
    chain: np.ndarray,
    image_size_px: int,
    pixel_size_nm: float,
    dna_height_nm: float = 2.0,
    dna_width_nm: float = 2.0,
    crossing_height_factor: float = 2.0,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Return (height_nm, mask, skeleton), each shape (image_size_px, image_size_px). TODO."""
    raise NotImplementedError
