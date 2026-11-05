"""AFM tip shapes and tip convolution.

The measured image is the grey-scale dilation of the true surface by the reflected tip:
    image(x) = max_u [ surface(x - u) - tip(u) ]
This makes DNA look wider than it is. Keep this module differentiable-friendly so the same
operator can later be used as a layer (see Idea 2: physics-based tracing).
"""

from __future__ import annotations

import numpy as np


def make_tip(shape: str, radius_nm: float, pixel_size_nm: float, half_width_px: int = 15) -> np.ndarray:
    """Tip height profile on a (2h+1, 2h+1) grid, apex at 0, increasing outward. TODO."""
    raise NotImplementedError


def dilate(height: np.ndarray, tip: np.ndarray) -> np.ndarray:
    """Grey-scale dilation of a height map by a tip. TODO (skimage or scipy.ndimage)."""
    raise NotImplementedError
